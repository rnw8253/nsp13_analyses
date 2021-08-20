import numpy as np
import sys

# RNA  Prob
labels1 = np.loadtxt("../gmm_lda/labels.dat")[:1199794]
labels2 = np.loadtxt("../gmm_lda/labels.dat")[1199794:]
weights1 = np.loadtxt("../reweight/rna_weights.dat")[:,0]
weights2 = np.loadtxt("../reweight/rna_atp_weights.dat")[:,0]
labels1.astype(int)
labels2.astype(int)
nLabels1 = len(labels1)
nLabels2 = len(labels2)
nClusts = len(np.unique((labels1)))
print(nClusts)
tot1 = np.sum(weights1)
tot2 = np.sum(weights2)

out = open("cluster.probability.dat",'w')
for i in range(nClusts):
    out.write("Cluster %s  %5.2f  %5.2f  %5.2f  %5.2f\n" %(i+1,len(labels1[labels1==i])*100/nLabels1,np.sum(weights1[labels1==i])*100/tot1,len(labels2[labels2==i])*100/nLabels2,np.sum(weights2[labels2==i])*100/tot2))
out.close

   



