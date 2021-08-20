import numpy as np
import sys


rna_labels = np.loadtxt("../reweight/rna.labels.dat")
rna_lda = np.loadtxt("../reweight/rna.lda.dat")
rna_labels = rna_labels.astype(int)
rna_atp_labels = np.loadtxt("../reweight/rna_atp.labels.dat")
rna_atp_lda = np.loadtxt("../reweight/rna_atp.lda.dat")
rna_atp_labels = rna_atp_labels.astype(int)


ru_labels = np.unique(rna_labels)
r_avg = []
out = open("rna.centers.dat",'w')
for lab in ru_labels:
    avg = np.average(rna_lda[rna_labels==lab],axis=0)
    r_avg.append(avg)
    out.write("  %2i" %(lab+1))
    for j in range(len(avg)):
        out.write("  %12.8f" %(avg[j]))
    out.write("\n")
out.close

r_nDists = []
for i in range(1,7):
    nDists = np.loadtxt("../../rna/data/rna.run0%i.distances.dat" %(i))
    r_nDists.append(len(nDists))

count = 0
rep = 1
min = np.full(len(ru_labels),1000.0)
index = np.zeros(len(ru_labels),dtype=int)
for i in range(len(rna_lda)):
    for j,lab in enumerate(ru_labels):
        if rna_labels[i] == lab:
            dist = np.linalg.norm(rna_lda[i][:1]-r_avg[j][:1])
            if dist < min[j]:
                min[j] = dist
                index[j] = i
print(r_nDists)
                
out = open("rna.frames.dat",'w')
for k,lab in enumerate(ru_labels):
    ind = index[k]
    flag = False
    rep = 0
    count = 0
    for j in range(len(r_nDists)):
        if flag == False:
            ind -= r_nDists[j] 
            rep += 1 
            if ind < 0:
                frame = ind + r_nDists[j]
                break
    out.write("  %i  %i  %i  %i\n" %(lab,rep,frame,index[k]))
out.close

#############################33

ru_labels = np.unique(rna_atp_labels)
r_avg = []
out = open("rna_atp.centers.dat",'w')
for lab in ru_labels:
    avg = np.average(rna_atp_lda[rna_atp_labels==lab],axis=0)
    r_avg.append(avg)
    out.write("  %2i" %(lab+1))
    for j in range(len(avg)):
        out.write("  %12.8f" %(avg[j]))
    out.write("\n")
out.close

r_nDists = []
for i in range(1,4):
    nDists = np.loadtxt("../../rna_atp/data/rna_atp.run0%i.distances.dat" %(i))
    r_nDists.append(len(nDists))

count = 0
rep = 1
min = np.full(len(ru_labels),1000.0)
index = np.zeros(len(ru_labels),dtype=int)
for i in range(len(rna_atp_lda)):
    for j,lab in enumerate(ru_labels):
        if rna_atp_labels[i] == lab:
            dist = np.linalg.norm(rna_atp_lda[i]-r_avg[j])
            if dist < min[j]:
                min[j] = dist
                index[j] = i
print(r_nDists)
                
out = open("rna_atp.frames.dat",'w')
for k,lab in enumerate(ru_labels):
    ind = index[k]
    flag = False
    rep = 0
    count = 0
    for j in range(len(r_nDists)):
        if flag == False:
            ind -= r_nDists[j] 
            rep += 1 
            if ind < 0:
                frame = ind + r_nDists[j]
                break
    out.write("  %i  %i  %i  %i\n" %(lab,rep,frame,index[k]))
out.close

    
