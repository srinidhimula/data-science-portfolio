"""Script contains the filters and checks based on point group for checking convergence in Piezoelectric constant value 'e'.
These functions are used to call from another script"""
import numpy as np
import pandas as pd

def echecks_pointgroup_zeroconv(df1,pg,pg_loc,zero_conv):
    #zero_conv=pow(10,-3)
    if pg=='1':
        for count,l in enumerate(pg_loc):
            df1.at[l,"Status_zeroconvergence"]="This sg doesnt have any"
    if pg=='2':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
                #print (" not zero 21",df1.at[l,'e21'],df1.at[l,"info_MOFCode"])
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e15'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e15"
            if abs(df1.at[l,'e24'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e24"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e31'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e31"
            if abs(df1.at[l,'e32'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e32"
            if abs(df1.at[l,'e33'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e33"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='m':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e14'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e14"
                #print (" not zero 21",df1.at[l,'e21'],df1.at[l,"info_MOFCode"])
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e25'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e25"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='222':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
                #print (" not zero 21",df1.at[l,'e21'],df1.at[l,"info_MOFCode"])
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e15'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e15"
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e24'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e24"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e31'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e31"
            if abs(df1.at[l,'e32'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e32"
            if abs(df1.at[l,'e33'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e33"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='mm2':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e14'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e14"
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e25'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e25"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='3':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='32':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e15'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e15"
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e24'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e24"
            if abs(df1.at[l,'e31'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e31"
            if abs(df1.at[l,'e32'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e32"
            if abs(df1.at[l,'e33'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e33"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='3m':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e14'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e14"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e25'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e25"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if (pg=='6') or (pg=='4'):
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if (pg=='6mm') or (pg=='4mm'):
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e14'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e14"
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e25'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e25"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='-6':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e14'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e14"
            if abs(df1.at[l,'e15'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e15"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e25'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e25"
            if abs(df1.at[l,'e24'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e24"
            if abs(df1.at[l,'e31'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e31"
            if abs(df1.at[l,'e32'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e32"
            if abs(df1.at[l,'e33'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e33"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='-6m2':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e14'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e14"
            if abs(df1.at[l,'e15'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e15"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e25'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e25"
            if abs(df1.at[l,'e24'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e24"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e31'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e31"
            if abs(df1.at[l,'e32'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e32"
            if abs(df1.at[l,'e33'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e33"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='-4':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e33'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e33"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if pg=='-42m':
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e15'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e15"
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e24'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e24"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e31'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e31"
            if abs(df1.at[l,'e32'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e32"
            if abs(df1.at[l,'e33'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e33"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if (pg=='23') or (pg=='-43m'):
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e15'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e15"
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e24'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e24"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e31'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e31"
            if abs(df1.at[l,'e32'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e32"
            if abs(df1.at[l,'e33'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e33"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    if (pg=='622') or (pg=='422'):
        for count,l in enumerate(pg_loc):
            if abs(df1.at[l,'e11'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e11"
            if abs(df1.at[l,'e12'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e12"
            if abs(df1.at[l,'e13'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e13"
            if abs(df1.at[l,'e15'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e15"
            if abs(df1.at[l,'e16'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e16"
            if abs(df1.at[l,'e21'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e21"
            if abs(df1.at[l,'e22'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e22"
            if abs(df1.at[l,'e23'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e23"
            if abs(df1.at[l,'e24'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e24"
            if abs(df1.at[l,'e26'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e26"
            if abs(df1.at[l,'e31'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e31"
            if abs(df1.at[l,'e32'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e32"
            if abs(df1.at[l,'e33'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e33"
            if abs(df1.at[l,'e34'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e34"
            if abs(df1.at[l,'e35'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e35"
            if abs(df1.at[l,'e36'])>=zero_conv:
                df1.at[l,"Status_zeroconvergence"]="Failed at e36"
            else:
                df1.at[l,"Status_zeroconvergence"]="Success at all eik"
    return df1


def echecks_pointgroup_depconv(df1,pg,pg_loc,dep_conv):
    #dep_conv=pow(10,-3)
    if pg=='1':
        for count,l in enumerate(pg_loc):
            df1.at[l,"Status_dependentconv"]="This sg doesnt have any"
    if pg=='2':
        for count,l in enumerate(pg_loc):
            df1.at[l,"Status_dependentconv"]="This sg doesnt have any"
    if pg=='m':
        for count,l in enumerate(pg_loc):
            df1.at[l,"Status_dependentconv"]="This sg doesnt have any"
    if pg=='222':
        for count,l in enumerate(pg_loc):
            df1.at[l,"Status_dependentconv"]="This sg doesnt have any"
    if pg=='mm2':
        for count,l in enumerate(pg_loc):
            df1.at[l,"Status_dependentconv"]="This sg doesnt have any"
    if pg=='3':
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e12'])-abs(df1.at[l,'e11']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e12"
            if abs(abs(df1.at[l,'e16'])-abs(df1.at[l,'e22']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e16"
            if abs(abs(df1.at[l,'e21'])-abs(df1.at[l,'e22']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e21"
            if abs(abs(df1.at[l,'e24'])-abs(df1.at[l,'e15']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e24"
            if abs(abs(df1.at[l,'e25'])-abs(df1.at[l,'e14']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e25"
            if abs(abs(df1.at[l,'e26'])-abs(df1.at[l,'e11']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e26"
            if abs(abs(df1.at[l,'e32'])-abs(df1.at[l,'e31']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e32"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if pg=='32':
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e12'])-abs(df1.at[l,'e11']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e12"
            if abs(abs(df1.at[l,'e25'])-abs(df1.at[l,'e14']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e25"
            if abs(abs(df1.at[l,'e26'])-abs(df1.at[l,'e11']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e26"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if pg=='3m':
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e16'])-abs(df1.at[l,'e22']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e16"
            if abs(abs(df1.at[l,'e21'])-abs(df1.at[l,'e22']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e21"
            if abs(abs(df1.at[l,'e24'])-abs(df1.at[l,'e15']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e24"
            if abs(abs(df1.at[l,'e32'])-abs(df1.at[l,'e31']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e32"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if (pg=='6') or (pg=='4'):
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e24'])-abs(df1.at[l,'e15']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e24"
            if abs(abs(df1.at[l,'e25'])-abs(df1.at[l,'e14']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e25"
            if abs(abs(df1.at[l,'e32'])-abs(df1.at[l,'e31']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e32"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if (pg=='6mm') or (pg=='4mm'):
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e24'])-abs(df1.at[l,'e15']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e24"
            if abs(abs(df1.at[l,'e32'])-abs(df1.at[l,'e31']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e32"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if pg=='-6':
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e12'])-abs(df1.at[l,'e11']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e12"
            if abs(abs(df1.at[l,'e16'])-abs(df1.at[l,'e22']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e16"
            if abs(abs(df1.at[l,'e21'])-abs(df1.at[l,'e22']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e21"
            if abs(abs(df1.at[l,'e26'])-abs(df1.at[l,'e11']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e26"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if pg=='-6m2':
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e16'])-abs(df1.at[l,'e22']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e16"
            if abs(abs(df1.at[l,'e21'])-abs(df1.at[l,'e22']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e21"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if pg=='-4':
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e24'])-abs(df1.at[l,'e15']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e24"
            if abs(abs(df1.at[l,'e25'])-abs(df1.at[l,'e14']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e25"
            if abs(abs(df1.at[l,'e32'])-abs(df1.at[l,'e31']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e32"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if pg=='-42m':
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e25'])-abs(df1.at[l,'e14']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e25"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if (pg=='23') or (pg=='-43m'):
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e25'])-abs(df1.at[l,'e14']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e25"
            if abs(abs(df1.at[l,'e36'])-abs(df1.at[l,'e14']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e36"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    if (pg=='622') or (pg=='422'):
        for count,l in enumerate(pg_loc):
            if abs(abs(df1.at[l,'e25'])-abs(df1.at[l,'e14']))>=dep_conv:
                df1.at[l,"Status_dependentconv"]="Failed at e25"
            else:
                df1.at[l,"Status_dependentconv"]="Success at all eik"
    return df1
