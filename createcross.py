# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:46:50 2017

@author: lenovo
"""

import numpy as np
import pandas as pd
from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20)
start = datetime.now()
newdata = np.genfromtxt('C:\\Users\\lenovo\\Desktop\\data\\1-5score.csv',delimiter=',')

chang = newdata.shape

te = np.random.randint(5,size=(chang[0]))

e1 = np.array(newdata)
e2 = np.array(newdata)
e3 = np.array(newdata)
e4 = np.array(newdata)
e5 = np.array(newdata)

e11 = np.zeros((1,3))
e22 = np.zeros((1,3))
e33 = np.zeros((1,3))
e44 = np.zeros((1,3))
e55 = np.zeros((1,3))

for i in range(chang[0]):
    if te[i] == 0:
        e1[i,2] = 0
        temp = newdata[i:i+1,0:3]
        e11 = np.concatenate((e11,temp),axis=0)
    if te[i] == 1:
        e2[i,2] = 0
        temp = newdata[i:i+1,0:3]
        e22 = np.concatenate((e22,temp),axis=0)
    if te[i] == 2:
        e3[i,2] = 0
        temp = newdata[i:i+1,0:3]
        e33 = np.concatenate((e33,temp),axis=0)
    if te[i] == 3:
        e4[i,2] = 0
        temp = newdata[i:i+1,0:3]
        e44 = np.concatenate((e44,temp),axis=0)
    if te[i] == 4:
        e5[i,2] = 0
        temp = newdata[i:i+1,0:3]
        e55 = np.concatenate((e55,temp),axis=0)



    
    
e11 = np.delete(e11,0,axis=0)  
e22 = np.delete(e22,0,axis=0)  
e33 = np.delete(e33,0,axis=0)  
e44 = np.delete(e44,0,axis=0)  
e55 = np.delete(e55,0,axis=0)    
    
end = datetime.now()

time = end - start

print(start)
print(end)
print(time)

np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi1.txt',e1,delimiter=' ')
np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi2.txt',e2,delimiter=' ')
np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi3.txt',e3,delimiter=' ')
np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi4.txt',e4,delimiter=' ')
np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi5.txt',e5,delimiter=' ')

np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi11.txt',e11,delimiter=' ')
np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi22.txt',e22,delimiter=' ')
np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi33.txt',e33,delimiter=' ')
np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi44.txt',e44,delimiter=' ')
np.savetxt('C:\\Users\\lenovo\Desktop\\tensor\\fi55.txt',e55,delimiter=' ')
