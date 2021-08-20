import numpy as np
import sys


labels = np.loadtxt("labels.dat")
lda = np.loadtxt("lda.dat")
labels = labels.astype(int)

nClusts = len(np.unique(labels))
nLDA = len(lda[0])
avg = np.zeros((nClusts,nLDA),dtype=float)

for i in range(nClusts):
    avg[i] = np.average(lda[labels==i],axis=0)

cols = np.arange(nClusts)+6
avg_dists = np.loadtxt("../contacts/avg_distances.dat",usecols=cols)

out = open("frames.dat",'w')
minDist = np.full(nClusts,10000)
minRun = np.zeros(nClusts,dtype=int)
minFrame = np.zeros(nClusts,dtype=int)
minRep = np.zeros(nClusts,dtype=int)
for i in range(1,7):
    dists = np.loadtxt("../../rna/data/rna.run0%i.distances.dat" %(i))
    for j in range(len(dists)):
        for k in range(nClusts):
            d = np.linalg.norm(dists[j] - avg_dists[:,k])
            if d < minDist[k]:
                minFrame[k] = j
                minDist[k] = d
                minRep[k] = i
for i in range(nClusts):
    out.write("  %3i  %3i  %10i\n" %(i+1,minRep[i],minFrame[i]))
out.write("\n\n\n")
minDist = np.full(nClusts,10000)
minRun = np.zeros(nClusts,dtype=int)
minFrame = np.zeros(nClusts,dtype=int)
minRep = np.zeros(nClusts,dtype=int)
for i in range(1,4):
    dists = np.loadtxt("../../rna_atp/data/rna_atp.run0%i.distances.dat" %(i))
    for j in range(len(dists)):
        for k in range(nClusts):
            d = np.linalg.norm(dists[j] - avg_dists[:,k])
            if d < minDist[k]:
                minFrame[k] = j
                minDist[k] = d
                minRep[k] = i
for i in range(nClusts):
    out.write("  %3i  %3i  %10i\n" %(i+1,minRep[i],minFrame[i]))
out.write("\n\n\n")

out = open("cluster_centers.dat",'w')
for i in range(nClusts):
    out.write("  %2i" %(i+1))
    for j in range(nLDA):
        out.write("  %12.8f" %(avg[i,j]))
    out.write("\n")
out.close
