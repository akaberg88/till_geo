# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:27:46 2016

@author: root
"""

import glob

#Tämä on esimerkistä Copying selected lines of (multiple) files into a new location
source_dir = "/home/geo/data/kersilo"
till_paths = glob.glob(source_dir + "/outside_all.csv")

#Tämä on esimerkistä Interacting with our file data
with open("outside_all.csv", "r") as infile:
    data = infile.read()
    datalist = data.splitlines()

#Tehdään sarakkeista omat listat
Numb = []
ID = []
Sedi = []  
Depth = []
X = []
Y = []
Multit = []
Profile = []
Prof_end = []
Ssorted = []
# MUISTA ETTÄ OUTSIDE.CSV EI OLE Numb SARAKETTA
for i in range(1,len(datalist)):
    line = datalist[i]
    splitline = line.split(",")
    Numb.append(splitline[0])
    ID.append(splitline[1])
    Sedi.append(splitline[2])
    Depth.append(splitline[3])
    X.append(splitline[4])
    Y.append(splitline[5])
    Profile.append(splitline[6])
    Prof_end.append(splitline[7])
    Ssorted.append(splitline[8])
    
#for j in range(1,len(datalist)):
#    rivi = splitline[0]
#   if  X == X
#        for k in rivi[3]
#        print(Numb)

#for k in range(1,len(Sedi)):
#        if Sedi[k] == 'moreeni':            
#            print(Numb[k])     
#        else:
#            print('No')


joo = 'Yes'
ei = 'No'
#Tällä koodataan profiilin alin kerros ja ID          
#for d in range(1,len(Sedi)-1):
#    if X[d] != X[d+1]:
#        joo = joo * d
#        print(ID[d],joo)
#    elif X[d] == X[d+1]:
#        ei = ei
#        print(ID[d],ei)
        
#for a in range(1,len(Sedi)-1):
#    for u in range(1):
#        if X[a] != X[a+1]:
#            print(ID[a],joo)
#        elif X[a] == X[a+1]:    
#            print(ID[a],ei) 
            
#print(joo)

multi = ""

    
  
  

#for w in range(1,len(Sedi)-1):
#    multi = multi + ID[w] + Sedi[w] + str(Sedi[w]) +'\n'

print(multi)   
            
#kokeile for loopin edelle def-funktiota tai määitä jokin muuttuja
with open('till_all.txt', 'w') as out_file:
#    out_file.write(multi) # tämä sivulta http://stackoverflow.com/questions/25023233/how-to-save-python-screen-output-to-a-text-file
#    out_file.close       
    for a in range(1,len(Sedi)-1):        
            if X[a] != X[a+1]:
                out_file.write(joo+'\n')
            elif X[a] == X[a+1]:    
                out_file.write(ei+'\n') 
    out_file.close        