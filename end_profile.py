# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:27:46 2016

@author: Annika Åberg
Koodi etsii kohdennetun moreenilinjageokemian aineiston 
(GTK) alimman profiiliin kuuluvan näytteen perustuen X ja 
Y -koordinaatteihin.
"""

import glob

#Työskentelykansion määritys
source_dir = "/home/geo/data/kersilo"
till_paths = glob.glob(source_dir + "/outside_all.csv")

#Tulostiedoston määritys
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
# Tässä muutetaan rivit listoiksi
for i in range(0,len(datalist)):
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
    
joo = 'Yes'
ei = 'No'

#Tässä kirjoitetaan profiilin päättyminen tulos tiedostoon.
with open('end_profile.csv', 'w') as out_file:
    for a in range(1,len(Sedi)-1):        
            if X[a] != X[a+1] or Y[a] != Y[a+1]:
                yes_line = str(ID[a])+','+str(Sedi[a])+','+str(Depth[a])+','+str(X[a])+','+str(Y[a])+','+joo+'\n'                                
                out_file.write(yes_line)
            elif X[a] == X[a+1] or Y[a] != Y[a+1]:  
                no_line = str(ID[a])+','+str(Sedi[a])+','+str(Depth[a])+','+ str(X[a])+','+str(Y[a])+','+ei+'\n'              
                out_file.write(no_line) 
                out_file.close        