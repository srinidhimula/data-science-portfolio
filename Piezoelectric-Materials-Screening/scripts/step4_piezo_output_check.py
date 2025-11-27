from pymatgen.io.vasp.outputs import *
import numpy as np
import pandas as pd
from pathlib import Path
from vasptonorm import main_vasptopiezonorm


class PiezoOutputCheck():
    def __init__(self,maindir,calcdir,failed_optfinal,mofrefcodes):
        self.maindir = Path(maindir)
        self.calcdir=Path(calcdir)
        self.failed_piezo=[]
        self.failed_optfinal=failed_optfinal
        self.mofrefcodes=mofrefcodes


    def checkpiezo_outcar(self):
        for subdir in self.calcdir.iterdir():
            if subdir.is_dir():
                outcar_piezopath = self.calcdir / subdir.name /"piezo_isym"/ "OUTCAR"

                if outcar_piezopath.exists():
                    with open(outcar_piezopath, 'r') as file:
                        contents = file.read()
                        if "PIEZOELECTRIC TENSOR IONIC CONTR  for field in x, y, z        (C/m^2)" not in contents:
                            self.failed_piezo.append(subdir.name)
                else:
                    self.failed_piezo.append(subdir.name)
        print ("Piezoelectric calc dint work",self.failed_piezo)
        return (self.failed_piezo)

    def _clean_results_file(self, file_path):
        with open(file_path, 'r') as f:
            content = f.read().replace("[", "").replace("]", "")
        with open(file_path, 'w') as f:
            f.write(content)

    def _extract_line_indices(self, lines):
        clamp_num = dynamic_num = total_e_num = norm_num = None
        for index, line in enumerate(lines):
            if "Clamped" in line:
                clamp_num = index
            elif "Dynamic" in line:
                dynamic_num = index
            elif "Piezo_e" in line:
                total_e_num = index
            elif "Norm" in line:
                norm_num = index
        return clamp_num, dynamic_num, total_e_num, norm_num

    def _build_dataframe(self, matrix, mof_code, norm, norm_colname, piezo_path):
        matrix = matrix.reshape(1, -1)
        colnames = [f"e{i+1}{j+1}" for i in range(3) for j in range(6)]
        df = pd.DataFrame(matrix, columns=colnames)
        df["info_MOFCode"] = mof_code
        df.set_index("info_MOFCode", inplace=True)
        df[norm_colname] = norm

        point_group = self.mofrefcodes[np.where(self.mofrefcodes[:, 0] == mof_code), 2]
        df["info_PointGroup"] = point_group[0][0] if point_group.size > 0 else "Unknown"

        pos = Poscar.from_file(piezo_path / "POSCAR", check_for_POTCAR=False)
        atoms = "-".join([f"{el}{n}" for el, n in zip(pos.site_symbols, pos.natoms)])
        df["info_Atoms"] = atoms

        if piezo_path.parent.joinpath("INCAR").exists():
            with open(piezo_path.parent / "INCAR") as f:
                content = f.read()
                if "ISPIN = 2" in content:
                    print("ISPIN = 2 exists for", mof_code)
                    try:
                        mag_opt = Outcar(piezo_path.parent / "OUTCAR").total_mag
                        mag_piezo = Outcar(piezo_path / "OUTCAR").total_mag
                        df["info_optnetmagmom"] = mag_opt
                        df["info_piezonetmagmom"] = mag_piezo
                    except Exception as e:
                        print(f"Warning: Could not extract magnetic moments for {mof_code} - {e}")
                        df["info_optnetmagmom"] = 0
                        df["info_piezonetmagmom"] = 0
                else:
                    df["info_optnetmagmom"] = 0
                    df["info_piezonetmagmom"] = 0
        return df


    def extractpiezo_data(self):
        for mof_dir in self.calcdir.iterdir():
            print (mof_dir)
            if not mof_dir.is_dir():
                continue
            mof_code = mof_dir.name
            #print ("mof_code",mof_code)
            if mof_code in self.failed_piezo:
                print("Piezo didn't finish properly:", mof_code)
                continue
            if mof_code not in self.failed_optfinal and mof_code not in self.failed_piezo:
                piezo_path = mof_dir / "piezo_isym"
                if piezo_path.is_dir():
                    os.chdir(piezo_path)
                    main_vasptopiezonorm(piezo_path/"OUTCAR",file_results="results.txt")
                    self._process_results(piezo_path, mof_code)

    def _process_results(self, piezo_path, mof_code):
        results_txt = piezo_path / "results.txt"
        self._clean_results_file(results_txt)
        with open(results_txt, 'r') as f:
            lines = f.readlines()

        clamp_num, dynamic_num, total_e_num, norm_num = self._extract_line_indices(lines)
        clamped_norm, dynamic_norm, total_e_norm = lines[norm_num].split()[-3:]
        results_matrix = [np.zeros((3, 6)) for _ in range(3)]
        line_indices = [clamp_num, dynamic_num, total_e_num]

        for l, start_idx in enumerate(line_indices):
            for row_idx in range(start_idx + 1, start_idx + 4):
                values = list(map(float, lines[row_idx].split()))
                results_matrix[l][row_idx - (start_idx + 1)] = values

        norm_list = [clamped_norm, dynamic_norm, total_e_norm]
        norm_names = ["info_ClampedNorm", "info_DynamicNorm", "info_TotaleNorm"]
        csv_names = ["clamped.csv", "dynamic.csv", "totale.csv"]

        for i, (matrix, norm, norm_name, csv_name) in enumerate(zip(results_matrix, norm_list, norm_names, csv_names)):
            df = self._build_dataframe(matrix, mof_code, norm, norm_name, piezo_path)
            csv_path = self.maindir / csv_name

            # Check if DataFrame is not None or empty
            if df is not None and not df.empty:
                mof_code = df.index[0] if df.index.name == "info_MOFCode" else df["info_MOFCode"].values[0]

                # If CSV exists, read and check for duplicate
                if csv_path.exists():
                    existing_df = pd.read_csv(csv_path, index_col=0 if df.index.name == "info_MOFCode" else None)

                    if mof_code in (existing_df.index if df.index.name == "info_MOFCode" else existing_df["info_MOFCode"].values):
                        print(f"{mof_code} already in {csv_name}, skipping")
                    else:
                        df.to_csv(csv_path, mode='a', header=False)
                        print ("Writing results to:",csv_names)
                else:
                    df.to_csv(csv_path, mode='w', header=True)
                    print ("Writing results to:",csv_names)
            else:
                print(f"Warning: DataFrame is None or empty for {mof_code}, norm: {norm_name}")

   