import numpy as np
import sys


dists = np.loadtxt("../data/distances.dat")
labels = np.loadtxt("../gmm_lda/labels.dat")
resFile = "../data/dist_list.dat"
f = open(resFile,'r')
res = f.readlines()
labels = labels.astype(int)

print(len(res))
nLab = len(np.unique(labels))
print(nLab)
nDist = len(dists[0])
print(nDist)
print(np.shape(dists))

avg = np.zeros((nLab,nDist),dtype=float)
std = np.zeros((nLab,nDist),dtype=float)
for i in range(nLab):
    avg[i] = np.average(dists[labels==i,:],axis=0)
    std[i] = np.std(dists[labels==i,:],axis=0)/np.sqrt(len(dists[labels==i,:]))

out1 = open("avg_distances.dat",'w')
out2 = open("std_distances.dat",'w')

for i in range(nDist):
    temp = res[i].split()
    out1.write("  %3s  %3s  %3s  %3s  %3s  %3s" %(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5]))
    out2.write("  %3s  %3s  %3s  %3s  %3s  %3s" %(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5]))
    for j in range(nLab):
        out1.write("  %12.8f" %(avg[j,i]))
        out2.write("  %12.8f" %(std[j,i]))
    out1.write("\n")
    out2.write("\n")

out1.close
out2.close
