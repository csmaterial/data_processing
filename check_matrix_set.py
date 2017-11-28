
pannum = 0
us = 1
for i in range(len(newdata)):
    #
    
    
    if newdata[i,0] ==  us:
        if pannum == 0:
            sa = newdata[i:i+1,:]
            pannum+=1
        else:
            sa1 = newdata[i:i+1,:]
            sa=np.concatenate((sa,sa1),axis=0)
    else:
