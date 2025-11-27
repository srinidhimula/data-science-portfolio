import numpy as np
from pathlib import Path
import shutil
import os
from pymatgen.io.vasp import Poscar
from pymatgen.io.cif import CifWriter,CifParser
from pymatgen.core import IStructure
from pymatgen.io.vasp.inputs import Kpoints


class PiezoInputPreparer:
    def __init__(self, calcdir, failed_optfinal):
        self.calcdir = Path(calcdir)
        self.failed_optfinal = set(failed_optfinal)  # convert to set for faster lookup

    def prepare_all_piezo_inputs(self):
        os.chdir(self.calcdir)
        for mofdir in os.listdir('.'):
            if os.path.isdir(mofdir):
                if mofdir in self.failed_optfinal:
                    print("Opt did not finish properly:", mofdir)
                    continue

                path_opt = os.path.join(self.calcdir, mofdir)
                path_piezo = os.path.join(path_opt, 'piezo_isym')

                if os.path.isdir(path_piezo):
                    print("Piezo folder already exists:", mofdir)
                    continue

                print("Creating piezo input for:", mofdir)
                os.mkdir(path_piezo)

                # Copy necessary files
                self.copy_file(os.path.join(path_opt, 'CONTCAR'), os.path.join(path_piezo, 'POSCAR'))
                self.copy_file(os.path.join(path_opt, 'POTCAR'), os.path.join(path_piezo, 'POTCAR'))
                self.copy_file(os.path.join(path_opt, 'KPOINTS'), os.path.join(path_piezo, 'KPOINTS'))
                self.copy_file(os.path.join(path_opt, 'INCAR'), os.path.join(path_piezo, 'INCAR'))

                self.edit_incar_for_piezo(path_piezo)

    def copy_file(self, src, dst):
        if os.path.isfile(src):
            shutil.copy(src, dst)
        else:
            print(f"Warning: Missing file {src}")

    def edit_incar_for_piezo(self, path_piezo):
        incar_path = os.path.join(path_piezo, 'INCAR')
        if not os.path.isfile(incar_path):
            print("INCAR not found at", incar_path)
            return

        with open(incar_path, 'r') as f:
            lines = f.readlines()

        with open(incar_path, 'w') as f:
            for line in lines:
                if 'NSW' in line:
                    f.write(' #NSW = 400 \n')
                elif 'NCORE' in line:
                    f.write(' #NCORE = 32 \n')
                elif 'IBRION' in line:
                    f.write(' IBRION = 6 \n')
                elif 'ISIF' in line:
                    f.write(' ISIF = 2 \n')
                elif 'NELMIN' in line:
                    f.write(' #NELMIN = 3 \n')
                elif 'LWAVE' in line:
                    f.write(' LWAVE = .FALSE. \n')
                elif 'MAGMOM' in line:
                    f.write(' #MAGMOM \n')
                elif 'LAECHG' in line:
                    f.write(' LAECHG = .FALSE. \n')
                elif 'NELM' in line:
                    f.write(' NELM = 500 \n')
                else:
                    f.write(line)
            f.write('\n LEPSILON = .TRUE.\n')