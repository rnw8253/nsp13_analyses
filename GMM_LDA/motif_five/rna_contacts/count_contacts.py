import numpy as np
import sys

p1 = np.loadtxt("../data/phosphate.dat")
p2 = np.loadtxt("data/phosphate.dat")
dists = np.loadtxt("../data/rna.dat")
#dists2 = np.loadtxt("/home/ryan/Desktop/nsp13/analyses/motif_dist/rna_pocket/combined/data/distances.dat")

w = np.loadtxt("weights.dat")
labels = np.loadtxt("labels.dat")
labels.astype(int)
cutoff = 5.0
nDists = len(dists[0])
nFrames = len(dists)
lab = np.unique(labels)

per = np.zeros((len(lab),5),dtype=float)
for i in range(nFrames):
    flag = [False,False,False,False,False]
    for j in range(nDists):
        if dists[i,j] < cutoff:
            #ind = int(p1[i,j]-p2[i,0])
            ind = int(p2[i,1]-p1[i,j])
            if ind < 5:
                flag[ind] = True
    for j in range(5):
        if flag[j] == True:
            per[int(labels[i]),j] += w[i,0]
            #per[int(labels[i]),j] += 1

for i in range(len(lab)):
    per[i,:] /= np.sum(w[labels==i,0])
    #per[i,:] /= len(labels[labels==i])
per *= 100
out = open("rna_contacts.dat",'w')
for i in range(5):
    for l in range(len(lab)):
        out.write("  %5.2f" %(per[l,i]))
    out.write("\n")
out.close






