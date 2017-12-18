import numpy as np
import pandas as pd

def makenamelist(user):
        
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
    return (user,l)

def usercode(te,l):
    ugroup = []
    st = te[0,0]
    l = []
    for i in range(len(te)):
        if te[i,0] == st:
            l.append(i)
        else:
            ugroup.append(l)
            l = []
            st = te[i,0]
            l.append(i)    
    return ugroup

def wholel(ul,ugroup):  
    whole = []
    for i in ul:
        if len(whole) ==0:
            whole = ugroup[i-1]
        else:    
            tem = ugroup[i-1]
            whole = whole+tem
    return whole

def wholedata(ul,ugroup,te):
    
    whole = wholel(ul,ugroup)
    
    newdata = np.zeros((len(whole),te.shape[1]))
    n = 0
    for i in whole:
        newdata[n,:] = te[i,:]
        n+=1
    return newdata


         
te = np.genfromtxt('file',delimiter=',')



#trueid = l[int(user[i]-1)]
user = np.array(te[:,0])
(user,l) = makenamelist(user)


te[:,0] = user+1

#ugroup[user -1] 
ugroup = usercode(te,l)

ul = []
for i in range(50):
    ul.append(i+1)    

# the user in whole make the matrix
new = wholedata(ul,ugroup,te)
