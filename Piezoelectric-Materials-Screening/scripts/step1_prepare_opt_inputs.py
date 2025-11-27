
import numpy as np
from pathlib import Path
import shutil
import os
from pymatgen.io.vasp import Poscar
from pymatgen.io.cif import CifWriter,CifParser
from pymatgen.core import IStructure
from pymatgen.io.vasp.inputs import Kpoints

from findsym_becwork import main_findsym

#moflists="MOFnames.txt"


class VASPInputPreparer:
    def __init__(self, calcdir, potcar_path, density,
                 potcar_suffixes=None, qmofbase=None, moflist_file=None):
        self.calcdir = Path(calcdir)
        self.potcar_path = Path(potcar_path)
        self.density = density
        self.potcar_suffixes = potcar_suffixes or {}
        self.qmofbase = Path(qmofbase) if qmofbase else None
        self.moflist_file = Path(moflist_file) #if moflist_file else None
        self.mof_codes = []

    def create_mof_dirs(self):
        """Create subdirectories for MOF reference codes from list file"""
        if not self.moflist_file or not self.moflist_file.exists():
            print(f"MOF list file not found: {self.moflist_file}")
            return

        print("Creating MOF directories...")
        mofrefcodes = np.loadtxt(self.moflist_file, dtype=str)

        if mofrefcodes.ndim == 1:
            mof_names = mofrefcodes
        else:
            mof_names = mofrefcodes[:, 0]

        for mof_name in mof_names:
            mof_dir = self.calcdir / mof_name
            if mof_dir.exists():
                print(f"Directory exists: {mof_name}")
            else:
                mof_dir.mkdir(parents=True)
                print(f"Created directory: {mof_name}")

        self.mof_codes = mof_names
        print (self.mof_codes)

    def convert_contcar_to_poscar_sym(self):
        if not self.qmofbase or not self.mof_codes.any():
            print("Cannot proceed: qmofbase or mof_codes not set.")
            return

        print("Converting CONTCAR → POSCAR using symmetry...")

        try:
            mofrefcodes = np.loadtxt(self.moflist_file, dtype=str)
        except Exception as e:
            print(f"Error reading MOF list: {e}")
            return

        for mofname in self.mof_codes:
            folder = self.calcdir / mofname
            if not folder.is_dir():
                print(f"Skipping non-folder: {folder}")
                continue

            print(f"Entering: {mofname}")
            try:
                contcar_src = self.qmofbase / mofname / "CONTCAR"
                poscar_p1 = folder / "POSCAR_P1"
                shutil.copy(contcar_src, poscar_p1)

                p = Poscar.from_file(poscar_p1, check_for_POTCAR=False)
                cif_writer = CifWriter(p.structure)
                tmp_cif = folder / "tmp.cif"

                cif_writer.write_file(tmp_cif)
                #print(tmp_cif.read_text())

                sgnum = int(main_findsym(tmp_cif,folder))
                #print (sgnum)

                row_index = np.where(mofrefcodes[:, 0] == mofname)[0]
                if len(row_index) == 0:
                    print(f"No symmetry info found for {mofname}")
                    continue

                sg_label = mofrefcodes[row_index[0], 1]
                tmp_cif_sym = folder / f"tmp_{sg_label}.cif"

                parser = CifParser(tmp_cif_sym)
                structure = parser.get_structures()[0]
                #structure.to(filename=folder / f"tmp{sg_label}.cif", fmt="cif")
                structure.to(filename=folder / "POSCAR", fmt="poscar")

                print(f"Processed {mofname} → sgnum {sgnum}")

            except Exception as e:
                print(f"Error processing {mofname}: {e}")

    def prepare_all(self):
        print("Preparing VASP input files (POTCAR, KPOINTS, INCAR)")
        for subdir in self.calcdir.iterdir():
            if not subdir.is_dir():
                continue
            print(f"Processing: {subdir.name}")
            self.prepare_potcar(subdir)
            self.prepare_kpoints(subdir)
            if self.qmofbase:
                self.prepare_incar(subdir)

    def prepare_potcar(self, folder):
        poscar_file = folder / "POSCAR"
        potcar_file = folder / "POTCAR"
        try:
            atomline = poscar_file.read_text().splitlines()[5]
            atom_symbols = atomline.split()

            with potcar_file.open("w") as f:
                for symbol in atom_symbols:
                    suffix = self.potcar_suffixes.get(symbol, "")
                    potcar_source = self.potcar_path / f"{symbol}{suffix}" / "POTCAR"
                    try:
                        f.write(potcar_source.read_text())
                    except FileNotFoundError:
                        print(f"Missing POTCAR for {symbol} at {potcar_source}")
        except Exception as e:
            print(f"POTCAR error in {folder}: {e}")

    def prepare_kpoints(self, folder):
        poscar_file = folder / "POSCAR"
        kpoints_file = folder / "KPOINTS"
        try:
            struct = IStructure.from_file(str(poscar_file))
            kpts = Kpoints.automatic_density(struct, kppa=int(self.density), force_gamma=False)
            kpoints_file.write_text(str(kpts))
        except Exception as e:
            print(f"KPOINTS error in {folder}: {e}")

    def prepare_incar(self, folder):
        qmof_incar_path = self.qmofbase / folder.name / "INCAR"
        incar_dest = folder / "INCAR"
        if not qmof_incar_path.exists():
            print(f"INCAR template not found: {qmof_incar_path}")
            return

        shutil.copy(qmof_incar_path, incar_dest)

        try:
            lines = incar_dest.read_text().splitlines()
            with incar_dest.open("w") as f:
                for line in lines:
                    if "LCHARG" in line:
                        f.write(" LCHARG= .FALSE.\n")
                    elif "LASPH" in line:
                        f.write(" LASPH = .FALSE.\n")
                    elif "LWAVE" in line:
                        f.write(" LWAVE = .FALSE.\n")
                    elif "LAECHG" in line:
                        f.write(" LAECHG = .FALSE.\n")
                    elif "SYMPREC" in line:
                        f.write(" SYMPREC = 1.00E-05\n")
                    elif "ISYM" in line:
                        f.write(" ISYM = 2\n")
                    elif "NCORE" in line:
                        f.write(" NCORE = 16\n")
                    elif "EDIFF" in line:
                        f.write(" EDIFF = 1.00e-07\n")
                    elif "NSW" in line:
                        f.write(" NSW = 500\n")
                    else:
                        f.write(line + "\n")

                f.write("\n KPAR = 4\n")
                f.write(" NELMIN = 3\n")
                f.write(" IBRION = 2\n")
                f.write(" ISIF = 3\n")

        except Exception as e:
            print(f"INCAR error in {folder}: {e}")