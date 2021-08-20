import numpy as np
import sys

p1 = np.loadtxt("../data/phosphate.dat")
p2 = np.loadtxt("data/phosphate.dat")
dists = np.loadtxt("../data/rna.dat")
dists2 = np.loadtxt("data/distances.dat")
labels = np.loadtxt("labels.dat")
w = np.loadtxt("weights.dat")
cutoff = 5.0
nDists = len(dists[0])
nFrames = len(dists)

per = np.zeros((5,5),dtype=float)
norm = np.zeros(5,dtype=float)

for i in range(nFrames):
    IV_flag = False
    Ia_flag = False
    p_flag = False
    if dists2[i,0] < 7:
        IV_flag = True
    if dists2[i,2] < 7:
        Ia_flag = True
    if dists2[i,1] > 17.00:
        p_flag = True

    state = 4
    if IV_flag == True  and p_flag == True  and Ia_flag == True :
        state = 0                          
    if IV_flag == False and p_flag == True  and Ia_flag == True :
        state = 3                          
    if IV_flag == True  and p_flag == False and Ia_flag == True :
        state = 2                          
    if IV_flag == True  and p_flag == False and Ia_flag == False:
        state = 1
    if state == 4:
        print(dists2[i],IV_flag,p_flag,Ia_flag,labels[i])
    flag = [False,False,False,False,False]
    for j in range(nDists):
        if dists[i,j] < cutoff:
            ind = int(p2[i,1]-p1[i,j])
            if ind < 5:
                flag[ind] = True            
        
    for j in range(5):
        if flag[j] == True:
            per[state,j] += w[i,2]
    norm[state] += w[i,2]

print(norm)
for i in range(5):
    per[i,:] /= norm[i]

per *= 100
out = open("rna_contacts.dat",'w')
for i in range(5):
    for l in range(5):
        out.write("  %5.2f" %(per[l,i]))
    out.write("\n")
out.close






