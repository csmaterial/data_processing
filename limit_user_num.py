#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:19:10 2017

@author: czy
"""

import numpy as np
import pandas as pd

address = '/home/czy/num_beerdata.csv'
uaddress = '/home/czy/usernum.csv'
tempaddress  = '/home/czy/tempbeer.csv'
unum = pd.read_csv(uaddress)
ee = pd.read_csv(address)

newarr = np.zeros((len(ee),7))

newarr[:,0] = np.array(ee['user'])
newarr[:,1] = np.array(ee['item'])
newarr[:,2] = np.array(ee['app'])
newarr[:,3] = np.array(ee['aro'])
newarr[:,4] = np.array(ee['pal'])
newarr[:,5] = np.array(ee['tas'])
newarr[:,6] = np.array(ee['ove'])

 

uless = []
for i in range(len(unum)):
    if unum[i]<=2:
        uless.append(i)
count = 0
for i in range(len(newarr)):
    i = i-count
    te = newarr[i,0]
    if te in uless:
        newarr = np.delete(newarr,i,axis=0)
        count+=1

def makenamelist(user):        
    #user = ee[col]
    
    l = []
    
    for i in range(len(user)):
    #for i in range(100):
        te = user[i]
        #print(te)
        if te not in l:
            l.append(te)
        print('create list %s'%i)    
    for i in range(len(user)):
        te = user[i]
        num = l.index(te)
        user[i] = num
        print('find list %s'%i)    
    return user

#newarr[:,0] = makenamelist(newarr[:,0])
newarr[:,1] = makenamelist(newarr[:,1])

l = []   
user = newarr[:,0]
for i in range(len(user)):
#for i in range(100):
    te = user[i]
    #print(te)
    if te not in l:
        l.append(te)
    print('create list %s'%i)    
for i in range(len(user)):
    te = user[i]
    num = l.index(te)
    user[i] = num
    print('find list %s'%i)    



     
