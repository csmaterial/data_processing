# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:58:57 2017

@author: lenovo
"""

import pandas as pd
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt


e = pd.read_excel('C:\\Users\\lenovo\\Desktop\\newdata2.xlsx') 
for i in range(18):
    th = i+1
    deal = e[th]
    new = np.zeros(len(deal))
    l = []
    for i in range(len(deal)):
        try:
            num = int(deal[i])
            if num>10:
                tem = np.array(l)
                r = int(np.mean(tem))
                new[i] = r
                l.append(r)
            else:
                new[i] = num
                l.append(num)
        except:
            tem = np.array(l)
            r = int(np.mean(tem))
            new[i] = r
            l.append(r)
    e[th] = new
'''    
deal = e['b3']
new = np.zeros(len(deal))
for i in range(len(deal)):
    try:
        num = int(deal[i])
        new[i] = num
    except:
        new[i] = 1
e['b3'] = new
'''



