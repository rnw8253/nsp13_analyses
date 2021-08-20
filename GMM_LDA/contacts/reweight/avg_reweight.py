import numpy as np
import sys
import glob


# Constants
T = 300
kT = 0.001987*T

# Determine the number of distances
nClusters = len(glob.glob("dists.*.dat"))
nFrames = np.zeros(nClusters,dtype=float)
for i in range(1,nClusters+1):
    data = np.loadtxt("weights.%s.dat" %(i))
    nFrames[i-1] = len(data)

files = glob.glob("distributions/*.dat")
nDists = int(len(files)/nClusters)
print(nDists,nClusters,nFrames)


avg = np.zeros((nClusters,nDists),dtype=float)
std = np.zeros((nClusters,nDists),dtype=float)
# Determine the avg and std for each cluster and distance
for k in range(1,nClusters+1):
    for i in range(1,nDists+1):
        data = np.loadtxt("distributions/pmf.%s.%s.dat" %(k,i),skiprows=5)
        dx = data[1,0]-data[0,0]
        data[:,1] = np.exp(-data[:,1]/kT)
        data[:,1] /= np.sum(data[:,1])
        sum = 0
        av = 0
        count = 0
        for j in range(len(data)):
            av += data[j,0]*data[j,1]
            sum += data[j,1]
            count += 1
        av /= sum
        sd = 0
        for j in range(len(data)):
            sd += (data[j,0]-av)**2*data[j,1]/sum
        #sd = np.sqrt(sd)/np.sqrt(nFrames[k-1])
        sd = np.sqrt(sd)
        avg[k-1,i-1] = av
        std[k-1,i-1] = sd
                

# Read in distance pairs
file = open("../../data/dist_list.dat",'r')
lines = file.readlines()
        
        
dist_min = []
out = open("avg_distances_rw.dat",'w')


for j,line in enumerate(lines):
    temp = line.split()
    print(temp)
    # Write to file all pair distances
    out.write("  %3s %3s %3s -- %3s %3s %3s" %(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5]))
    for i in range(nClusters):
        if 1 <= std[i,j] < 10:
            out.write(" & %3i(%1i)" %(avg[i,j],round(std[i,j])))
        if 1 <= std[i,j]*10 < 10:
            out.write(" & %3.1f(%1i)" %(avg[i,j],round(std[i,j]*10)))
        if 1 <= std[i,j]*100 < 10:
            out.write(" & %4.2f(%1i)" %(avg[i,j],round(std[i,j]*100)))
        if 1 <= std[i,j]*1000 < 10:
            out.write(" & %5.3f(%1i)" %(avg[i,j],round(std[i,j]*1000)))
        if 1 <= std[i,j]*10000 < 10:
            out.write(" & %6.4f(%1i)" %(avg[i,j],round(std[i,j]*10000)))
        if 1 <= std[i,j]*100000 < 10:
            out.write(" & %7.5f(%1i)" %(avg[i,j],round(std[i,j]*100000)))
    out.write("\n")        
out.close
