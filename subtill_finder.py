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
"""
import glob
import numpy as np

#Defining the file path and source files
source_dir = "/home/geo/"
file_paths = glob.glob("/home/geo/till_geo_num.csv")

#Defining output file
sedi_out = "/home/geo/subtill_out.csv"

datas=np.loadtxt(fname ='till_geo_num.csv', delimiter = ',', skiprows = 1, usecols=(1,2,3,4,5))

ids = np.array(datas[:,0])
sedim = np.array(datas[:,1])
depth = np.array(datas[:,2])
x = np.array(datas[:,3])
y = np.array(datas[:,4])


joo = 'Covers sub-till sorted layer'
ei = 'No'

for i in range(len(sedim)-1):
    sub_cond = ((x[i] == x[i+1]) & (y[i] == y[i+1]) & (sedim[i] == 0)& (sedim[i+1] == 1))
    if sub_cond == True:
        line_joo = str(ids[i])+','+str(depth[i])+','+str(x[i])+','+ str(y[i])+','+str(sedim[i])+','+joo
        print(line_joo)
        with open (sedi_out,'a') as m:
            m.write(line_joo+'\n')
    else:
        line_ei = str(ids[i])+','+str(depth[i])+','+str(x[i]) +','+str(y[i])+','+str(sedim[i])+','+ei
        print(line_ei)
        with open (sedi_out,'a') as m:
            m.write(line_ei+'\n')
        



    