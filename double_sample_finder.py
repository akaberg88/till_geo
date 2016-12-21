# -*- coding: utf-8 -*-
"""
Date: Wed 23.11.2016

@author: Annika Åberg

This code finds douple samples,
"""
import os
os.getcwd()
os.chdir('C:\\HY-Data\AKABERG\documents\Python')
import glob
import numpy as np

#Defining the file path and source files
source_dir = "C:\HY-Data\AKABERG\documents\Python"
file_paths = glob.glob("C:\HY-Data\AKABERG\documents\Python\outside_all.csv")

#Defining output file
profile_out = "C:\HY-Data\AKABERG\documents\Python\Actually_no_profile3.csv"

datas=np.loadtxt(fname ='outside_all.csv',dtype = {'names': ('SAMPLE_ID', 'SOILTYPE','DEPTH_m', 'X_EUREF','Y_EUREF'),
                                                    'formats': ('S20','S20', 'f6','f12','f12')},
                                                    delimiter=',',skiprows=1, usecols=(1,2,3,4,5))

ids = []
sedim = []
depth = []
x = []
y = []

for z in range (len(datas)):
    line = datas[z]
    line_str = str(line)
    ids.append(line[0])
    sedim.append(line[1])
    depth.append(line[2])
    x.append(line[3])
    y.append(line[4])


joo = 'DOUPLE SAMPLE'
ei = 'No problem here'

for i in range(len(sedim)-1):
    if x[i] == x[i+1]  and y[i] == y[i+1] and depth[i] == depth[i+1]:
        if x[i+2]!=x[i] != x[i-1] and x[i+2]!= y[i] != y[i-1]:
            line_joo = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+joo
            print(line_joo)
            with open (profile_out,'a') as m:
                m.write(line_joo+'\n')
        else:
            line_ei = str(ids[i])+','+str(depth[i])+','+str(x[i]) +','+str(y[i])+','+str(sedim[i])+','+ei
            print(line_ei)
            with open (profile_out,'a') as m:
                m.write(line_ei+'\n')        
    else:
        line_ei = str(ids[i])+','+str(depth[i])+','+str(x[i]) +','+str(y[i])+','+str(sedim[i])+','+ei
        print(line_ei)
        with open (profile_out,'a') as m:
            m.write(line_ei+'\n')
