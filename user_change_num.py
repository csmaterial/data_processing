#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:26:12 2017

@author: czy
"""

import re
import numpy as np
import pandas as pd
address = '/home/czy/beerdata.csv'

ee = pd.read_csv(address)

def makenamelist(ee,col):
        
    user = ee[col]
    l = []
    
    for i in range(len(user)):
        te = user[i]
        #print(te)
        if te not in l:
            l.append(te)
        
    for i in range(len(user)):
        te = user[i]
        num = l.index(te)
        user[i] = num
    return user

#user = makenamelist(ee,'user')
item = makenamelist(ee,'item')

newaddress = '/home/czy/user_beerdata.csv'
ee.to_csv(newaddress)  

