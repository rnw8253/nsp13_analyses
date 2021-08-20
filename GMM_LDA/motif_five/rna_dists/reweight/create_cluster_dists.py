import numpy as np
import sys


labels = np.loadtxt("labels.dat")
nLabels = len(np.unique(labels))

dists = np.loadtxt("../../data/rna.dat")
weights = np.loadtxt("weights.dat")
print(labels)
for i in range(nLabels):
    np.savetxt("dists.%s.dat" %(i+1),dists[labels == i])
    np.savetxt("weights.%s.dat" %(i+1),weights[labels == i])
    
