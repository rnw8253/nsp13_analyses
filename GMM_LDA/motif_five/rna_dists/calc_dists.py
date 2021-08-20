import numpy as np
import sys


dists = np.loadtxt("../data/rna.dat")
labels = np.loadtxt("../rna_contacts/labels.dat")
res = ["Val 533","ASP 534","SER 535","SER 536","GLN 537","GLY 538","SER 539","GLU 540"]
labels = labels.astype(int)

nLab = len(np.unique(labels))
nDist = len(dists[0])

avg = np.zeros((nLab,nDist),dtype=float)
std = np.zeros((nLab,nDist),dtype=float)
for i in range(nLab):
    avg[i] = np.average(dists[labels==i,:],axis=0)
    std[i] = np.std(dists[labels==i,:],axis=0)/np.sqrt(len(dists[labels==i,:]))

out1 = open("avg_distances.dat",'w')
out2 = open("std_distances.dat",'w')

for i in range(nDist):
    out1.write("  %s" %(res[i]))
    out2.write("  %s" %(res[i]))
    for j in range(nLab):
        out1.write("  %12.8f" %(avg[j,i]))
        out2.write("  %12.8f" %(std[j,i]))
    out1.write("\n")
    out2.write("\n")

out1.close
out2.close
