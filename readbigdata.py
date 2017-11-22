#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:12:47 2017

@author: czy
"""
import re
import numpy as np
import pandas as pd
address = '/home/czy/beerdata.csv'


def open_txt(file_name,num):
    with open(file_name,'rb') as f:
        while True:
        #for i in range(num):
            line = f.readline()
            if not line:
                return
            yield line.strip()

def getthenum(tediv):
    for i in range(len(tediv)):
        if tediv[i] == '/':
            return tediv[0:i]
def dealwithte(te):
    for i in range(len(te)):
        if te[i] == ':':
            tediv = te[i+2:] 
            try:
                num = int(getthenum(tediv))
                return num
            except:
                return tediv
            
yb = r'(beer/)(.+)(:)'
yr = r'(review/)(.+)(:)'
username = []
#pro
itemname = []
#bee
app = []
aro = []
pal = []
tas = []
ove = []


for text in open_txt('/home/czy/temp/ratebeer.txt',65848):
    e = text
    try:
        te = str(e, encoding = "utf-8")
        #print (te)
        if te[0:4] == 'beer':
            idname=re.search(yb,te).group(2)
            #print(idname)
            if idname[0:3] == 'bee':
                for i in range(len(te)):
                    if te[i] == ':':
                        itemname.append(te[i+2:])
                    
                        
        elif te[0:4] == 'revi':
            idname=re.search(yr,te).group(2)
            #print(idname)
            if idname[0:3] == 'app':
                app.append(dealwithte(te))
            elif idname[0:3] == 'aro':
                aro.append(dealwithte(te))
            elif idname[0:3] == 'pal':
                pal.append(dealwithte(te))
            elif idname[0:3] == 'tas':
                tas.append(dealwithte(te))
            elif idname[0:3] == 'ove':
                ove.append(dealwithte(te))
            elif idname[0:3] == 'pro':
                username.append(dealwithte(te))
                if len(username) != len(app):
                    app = app[0:len(username)]
                    itemname = itemname[0:len(username)]
                    aro = aro[0:len(username)]
                    pal = pal[0:len(username)]
                    tas = tas[0:len(username)]
                    ove = ove[0:len(username)]
    except:
        #print(e)
        #print('Warning')
        1+1
     

tee = np.zeros((len(app),7))            
ee = pd.DataFrame(tee)   
ee[0] = username
ee[1] = itemname
ee[2] = app
ee[3] = aro
ee[4] = pal
ee[5] = tas
ee[6] = ove                    
         
ee.columns = ['user','item','app','aro','pal','tas','ove']
           
ee.to_csv(address)    



'''
fname = '/home/czy/temp/ratebeer.txt'
with open(fname, 'r') as f:  #打开文件
    first_line = f.readline()  #读第一行
    
f.close()


f=open('/home/czy/temp/ratebeer.txt','r')  
while 1:  
    l=f.readline()  
    if l=='':  
        break  
    ####  
    #l=l.split()  
f.close()  
'''
