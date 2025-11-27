#!/usr/bin/env python3
import numpy as np
from numpy import linalg as LA
np.set_printoptions(linewidth=np.inf)
np.set_printoptions(suppress=True)

def process_outcar(file_outcar,file_results):
    with open (file_outcar,"r")as f:
        lines=f.readlines()
        for index,line in enumerate(lines):
            if "PIEZOELECTRIC TENSOR (including local field effects)  for field in x, y, z        (C/m^2)" in line :
                #print (index, line.rstrip())
                #print ("now 5 lines")
                piezo_clamped=(lines[index:index+6])
            if "PIEZOELECTRIC TENSOR IONIC CONTR  for field in x, y, z        (C/m^2)" in line:
                #print (index, line.rstrip())
                #print ("now 5 lines")
                piezo_dynamic=(lines[index:index+6])
            if "TOTAL ELASTIC MODULI (kBar)" not in line:
                
                elas=False
            if "TOTAL ELASTIC MODULI (kBar)" in line:
                elas=True
                elastic_stiffness=(lines[index:index+9])
    #print (elas)
    results=open(file_results,"w")
    if elas==True:
        for item2 in elastic_stiffness:
            results.write(item2)
    for item in piezo_clamped:
        results.write((item))
    for item1 in piezo_dynamic:
        results.write(item1)
    
    results.close()
    return elas

def process_piezo(elas,file_results):
    idx=[0,1,2,4,5,3] ##vasp outputs piezo tensor in different order than general voigt notation. This takes care of that and rearranges the order
    piezo_clamp=np.loadtxt(file_results, dtype=str,skiprows=3,max_rows=3) #based on format of file this stores clamped as array
    piezo_clamp=piezo_clamp[:,1:]
    piezo_clamp=piezo_clamp.astype('float64')
    piezo_dynamic=np.loadtxt(file_results, dtype=str,skiprows=9,max_rows=3) #based on format of file this stores ionic as array
    #print (piezo_dynamic)
    piezo_dynamic=piezo_dynamic[:,1:]
    piezo_dynamic=piezo_dynamic.astype('float64')

    piezo_clamp=piezo_clamp[:,idx]
    piezo_dynamic=piezo_dynamic[:,idx]
    total_piezo_e=np.add(piezo_clamp,piezo_dynamic)

    #norm of e and d matrices
    clamp_norm=LA.norm(piezo_clamp,2)
    dynamic_norm=LA.norm(piezo_dynamic,2)
    totalpiezo_norm=LA.norm(total_piezo_e,2)

    if elas==True:
        elastic_stiffness= np.loadtxt("results.txt", dtype=str,skiprows=15,max_rows=6) #based on format of file this stores elasticity as array
        elastic_stiffness=elastic_stiffness[:,1:]
        elastic_stiffness=elastic_stiffness.astype('float64')*pow(10,8) #conversion kbar to Pa
        elastic_stiffness=elastic_stiffness[:,idx]
        elastic_stiffness=elastic_stiffness[idx,:]
        #print  ("elastic modulus GPa")
        #print (elastic_stiffness/pow(10,9)) #conversion Pa to GPa
        piezo_d= np.matmul(total_piezo_e,np.linalg.inv(elastic_stiffness))*pow(10,12) #conversion of C/N to pC/N
        piezo_d_norm=LA.norm(piezo_d,2)
        #print ("piezo d and norm")
        #print (piezo_d,piezo_d_norm)
    return piezo_clamp,piezo_dynamic,total_piezo_e,clamp_norm,dynamic_norm,totalpiezo_norm

##############################################
# Main program follows

def main_vasptopiezonorm(file_outcar,file_results):
    elas=process_outcar(file_outcar,file_results)
    clamp_e,dynamic_e,total_e,clamp_e_norm,dynamic_e_norm,total_e_norm=process_piezo(elas,file_results)
    #print (clamp_e,"\n",dynamic_e,"\n",total_e,"\n",clamp_e_norm,"\n",dynamic_e_norm,"\n",total_e_norm)
    results1=open(file_results,"w")
    results1.write("Clamped piezo e in C/m2"+"\n"+str(clamp_e))
    results1.write("\n"+"Dynamic piezo e in C/m2"+"\n"+str(dynamic_e))
    results1.write("\n"+"Piezo_e in C/m2"+"\n"+str(total_e))
    results1.write("\n"+"Norm of clamped, dynamic and final e in C/m2"+" "+str(clamp_e_norm)+" "+str(dynamic_e_norm)+" "+str(total_e_norm))
    if elas==True:
        results1.write("\n"+"Elastic modulus in GPa"+"\n"+str(elastic_stiffness/pow(10,9)))
        results1.write("\n"+"Piezo_d in pC/N"+"\n"+str(piezo_d))
        results1.write("\n"+"Norm of piezo_d in pC/N"+" "+str(piezo_d_norm))
    results1.close()