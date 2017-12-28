import numpy as np
import pandas as pd
e = pd.read_csv('C:\\Users\\lenovo\\Desktop\\CP\\dictionary.csv')
#SentiWordNet_3.0.0_20130122.txt

pos = e['PosScore']
neg = e['NegScore']
li = []
for i in range(len(pos)):
    te = pos[i]+neg[i]
    if te == 0:
        li.append(i)
data = e.drop(li)    
    
data.to_csv('C:\\Users\\lenovo\\Desktop\\CP\\without0dictionary.csv')    
