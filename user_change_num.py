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
    name =  pd.DataFrame(ee[col])
    user = pd.Series(ee[col])
    
    l = []
    
    for i in range(len(user)):
        te = user[i]
        #print(te)
        if te not in l:
            l.append(te)
        
    for i in range(len(user)):
        te = user[i]
        num = l.index(te)
        user[int(i)] = num
    return (user,name)

(item,itemname) = makenamelist(M1,'asin')


newaddress = '/home/czy/user_beerdata.csv'
ee.to_csv(newaddress)  

