# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 07:16:36 2016

@author: Annika Åberg
"""

import glob
import numpy as np

#Defining the file path and source files
source_dir = "/home/geo/"
file_paths = glob.glob("/home/geo/till_geo_num.csv")

#Defining output file
sedi_out = "/home/geo/error_out.csv"

datas=np.loadtxt(fname ='till_geo_num.csv', delimiter = ',', skiprows = 1, usecols=(1,2,3,4,5))

ids = np.array(datas[:,0])
sedim = np.array(datas[:,1])
depth = np.array(datas[:,2])
x = np.array(datas[:,3])
y = np.array(datas[:,4])

xe = 'Error in X'
xy = 'Error in Y'
pt = 'This profile is fine'
idi = 'This is profile'
el = 'End profile or no profile'

for i in range(len(x)-1):
    id_cond = ((x[i] == x[i+1]) & (y[i] == y[i+1]) & (ids[i] == ids[i+1]))
    id_dif = ((x[i] == x[i+1]) & (y[i] == y[i+1]) & (ids[i] != ids[i+1]))
#    x_dif =  ((x[i] != x[i+1]) & (y[i] == y[i+1]) & (ids[i] == ids[i+1]))
#    y_dif = ((x[i] == x[i+1]) & (y[i] != y[i+1]) & (ids[i] == ids[i+1]))
#    x_dif_id =  ((x[i] != x[i+1]) & (y[i] == y[i+1]) & (ids[i] != ids[i+1]))
#    y_dif_id = ((x[i] == x[i+1]) & (y[i] != y[i+1]) & (ids[i] != ids[i+1]))
#    non_pfl =  ((x[i] != x[i+1]) & (y[i] != y[i+1]) & (ids[i] != ids[i+1]))   
    if id_cond == True:
        line_joo = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+pt
        print(line_joo)
        with open (sedi_out,'a') as m:
            m.write(line_joo+'\n')
    elif id_dif == True:
        line_idi = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+idi
        print(line_idi)
        with open (sedi_out,'a') as m:
            m.write(line_idi+'\n')   
#    elif x_dif == True:
#        line_xdif = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+x_dif
#        print(line_xdif)
#        with open (sedi_out,'a') as m:
#            m.write(line_xdif+'\n')  
#    elif y_dif == True:
#        line_ydif = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+y_dif
#        print(line_ydif)
#        with open (sedi_out,'a') as m:
#            m.write(line_ydif+'\n')
#    elif x_dif_id == True:
#        line_xdifid = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+x_dif_id
#        print(line_xdifid)
#        with open (sedi_out,'a') as m:
#            m.write(line_xdifid+'\n')  
#    elif y_dif_id == True:
#        line_ydifid = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+y_dif_id
#        print(line_ydifid)
#        with open (sedi_out,'a') as m:
#            m.write(line_ydifid+'\n')
#    elif non_pfl == True:
#        line_nonpfl = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+non_pfl
#        print(line_nonpfl)
#        with open (sedi_out,'a') as m:
#            m.write(line_nonpfl+'\n')        
    else:
        line_el = str(ids[i])+','+str(depth[i])+','+str(x[i]) +','+str(y[i])+','+str(sedim[i])+','+el
        print(line_el)
        with open (sedi_out,'a') as m:
            m.write(line_el+'\n')