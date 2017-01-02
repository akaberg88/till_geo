# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:00:05 2016

@author: Annika Åberg

This code finds a till unit from targeting till geochemistry data 
that is overlain by sub-till sorted sediment unit.
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
sedi_out = "C:\HY-Data\AKABERG\documents\Python\Subtill_test2_6.csv"

datas=np.loadtxt(fname ='till_geo_num.csv', delimiter = ',', skiprows = 1, usecols=(1,2,3,4,5))

ids = np.array(datas[:,0])
sedim = np.array(datas[:,1])
depth = np.array(datas[:,2])
x = np.array(datas[:,3])
y = np.array(datas[:,4])


joo = 'Sub-till sorted layer'
ei = 'No'

for i in range(len(sedim)-1):
    sub_cond = ((x[i] == x[i-1]) & (y[i] == y[i-1]) & (sedim[i] == 1)& (sedim[i-1] == 0))
    sub_cond_2 = ((x[i-1] == x[i] == x[i-2]) & (y[i-1] == y[i] == y[i-2]) & (sedim[i-2] == 0) & (sedim[i] == 1)& (sedim[i-1] == 1))
    sub_cond_3 = ((x[i-2] == x[i] == x[i-1] == x[i-3]) & (y[i-2] == y[i] == y[i-1] == y[i-3]) & (sedim[i-3] == 0) & (sedim[i] == 1)& (sedim[i-1] == 1) & (sedim[i-2] == 1))
    if sub_cond == True:
        line_joo = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+joo
        print(line_joo)
        with open (sedi_out,'a') as m:
            m.write(line_joo+'\n')
    elif i >= 2: 
        if sub_cond_2 == True:
            line_joo = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+joo
            print(line_joo)
            with open (sedi_out,'a') as m:
                m.write(line_joo+'\n')
        else:
            line_ei = str(ids[i])+','+str(depth[i])+','+str(x[i]) +','+str(y[i])+','+str(sedim[i])+','+ei
            print(line_ei)
            with open (sedi_out,'a') as m:
                m.write(line_ei+'\n')
    elif i >= 3: # EI LÖYDY JOS KAIKKI ON PÄÄLLÄ, MUTTA TOIMII YKSINÄÄN (ONGELMA ELIF?) --> MAKSIMI 4 SUBTILL
        if sub_cond_3 == True:
            line_joo = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+joo
            print(line_joo)
            with open (sedi_out,'a') as m:
                m.write(line_joo+'\n')
        else:
            line_ei = str(ids[i])+','+str(depth[i])+','+str(x[i]) +','+str(y[i])+','+str(sedim[i])+','+ei
            print(line_ei)
            with open (sedi_out,'a') as m:
                m.write(line_ei+'\n')
    else:
        line_ei = str(ids[i])+','+str(depth[i])+','+str(x[i]) +','+str(y[i])+','+str(sedim[i])+','+ei
        print(line_ei)
        with open (sedi_out,'a') as m:
            m.write(line_ei+'\n')
        



    
