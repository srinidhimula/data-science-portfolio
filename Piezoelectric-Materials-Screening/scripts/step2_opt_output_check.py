from pymatgen.io.vasp.outputs import *
import numpy as np
import pandas as pd
from pathlib import Path
np.set_printoptions(linewidth=np.inf)
np.set_printoptions(suppress=True)


class OptOutputCheck():
    def __init__(self, calcdir,maindir):
        self.calcdir=Path(calcdir)
        self.maindir=Path(maindir)
        self.failed=[]
        self.failed_duensw = []

    def _read_incar_cutoff(self, incar_path, keyword):
        try:
            with open(os.path.join(incar_path, 'INCAR')) as f:
                for line in f:
                    if keyword in line:
                        return int(line.split('=')[1].strip())
        except:
            return None
        return None

    def checkopt_oszicar(self,calcdir):
        #print (self.failed)
        for subdir in self.calcdir.iterdir():
            if subdir.is_dir():
                oszicar_path = self.calcdir / subdir.name / "OSZICAR"
                incar_path= self.calcdir / subdir.name / "INCAR"
                if not oszicar_path.exists():
                    print(f"OSZICAR does not exist in {subdir}")
                    self.failed.append(subdir.name)
                    return

                try:
                    #print("in try")
                    with open(oszicar_path, 'r') as f:
                        linesOZ = f.readlines()

                    cutoff = self._read_incar_cutoff(incar_path, 'NELM')
                    counts = []

                    for line in linesOZ:
                        tokens = line.split()
                        if len(tokens) > 1 and tokens[1].isdigit():
                            counts.append(int(tokens[1]))

                    if not linesOZ or (cutoff in counts):
                        print(f"{subdir.name} failed due to cutoff match or empty OSZICAR")
                        self.failed.append(subdir.name)

                except Exception as e:
                    print(f"Error while processing {subdir.name}: {e}")
                    self.failed.append(subdir.name)

    def checkopt_outcar(self,calcdir):
        for subdir in self.calcdir.iterdir():
            if subdir.is_dir():
                outcar_path= self.calcdir / subdir.name / "OUTCAR"
                print (subdir.name,subdir)

                if outcar_path.exists():
                    with open(outcar_path, 'r') as file:
                        contents = file.read()
                        if "reached required accuracy - stopping structural energy minimisation" not in contents:
                            print ("Optimisation did not reach a convergence")
                            self.failed.append(subdir.name)
                else:
                    print ("OUTCAR not present")
                    self.failed.append(subdir.name)

            # Second check for NSW-based failures
            #print (self.failed)
            for f in self.failed:
                fpath = self.calcdir / f
                cutoff = self._read_incar_cutoff(fpath, 'NSW')
                counts = []

                osz_path = os.path.join(fpath, 'OSZICAR')
                if os.path.exists(osz_path):
                    linesOZ = open(osz_path, 'r').readlines()
                    if len(linesOZ) > 0:
                        for line in linesOZ:
                            try:
                                if line.split()[0].isdigit():
                                    counts.append(int(line.split()[0]))
                            except:
                                print(f"{f} HAS BAD OSZ")
                                self.failed_duensw.append(f)
                                break
                        if cutoff in counts and f not in self.failed_duensw:
                            self.failed_duensw.append(f)
                    else:
                        self.failed_duensw.append(f)
    
    def run_full_check(self):
        self.checkopt_outcar(self.calcdir)
        self.checkopt_oszicar(self.calcdir)
        print("check1, Opt failed in OUTCAR check:", self.failed)
        print("check2, Opt failed due to NSW in OSZICAR check:", self.failed_duensw)

        # Only consider completely failed cases
        # (Cases that failed just due to NSW reaching max, you can retry increasing the number of steps)
        failed_optfinal = list(set(self.failed) - set(self.failed_duensw))
        print("Final failed list (do not continue):", failed_optfinal)

        with open(str(self.maindir / "Failed_opt.txt"), 'w') as f:
            f.write("\n".join(failed_optfinal))
        with open(str(self.maindir / "Failed_duetoNSW.txt"), 'w') as f:
            f.write("\n".join(self.failed_duensw))
        return failed_optfinal
