# -*- coding: utf-8 -*-
"""
Date: Wed 23.11.2016

@author: Annika Åberg

Sediment codes:
    till, weathered bedrock till = 0
    sand, gravel, silt, clay = 1
    weathered bedrock = 2
    unknown = 3
"""
import os
os.getcwd()
os.chdir('C:\\HY-Data\AKABERG\documents\Python')
import glob
import numpy as np

#Defining the file path and source files
source_dir = "C:\HY-Data\AKABERG\documents\Python"
file_paths = glob.glob("C:\HY-Data\AKABERG\documents\Python\till_geo_num.csv")

#Defining output file
profile_out = "C:\HY-Data\AKABERG\documents\Python\profile_out.csv"

datas=np.loadtxt(fname ='till_geo_num.csv', delimiter = ',', skiprows = 1, usecols=(1,2,3,4,5))

ids = np.array(datas[:,0])
sedim = np.array(datas[:,1])
depth = np.array(datas[:,2])
x = np.array(datas[:,3])
y = np.array(datas[:,4])


joo = 'Profile'
ei = 'No profile'

for i in range(len(sedim)-1):
    if x[i] == x[i+1] and y[i] == y[i+1]:
        line_joo = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+joo
        print(line_joo)
        with open (profile_out,'a') as m:
            m.write(line_joo+'\n')
    elif x[i] == x[i-1]and y[i] == y[i-1]:
        line_joo = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+joo
        print(line_joo)
        with open (profile_out,'a') as m:
            m.write(line_joo+'\n')
    else:
        line_ei = str(ids[i])+','+str(depth[i])+','+str(x[i]) +','+str(y[i])+','+str(sedim[i])+','+ei
        print(line_ei)
        with open (profile_out,'a') as m:
            m.write(line_ei+'\n')
        


