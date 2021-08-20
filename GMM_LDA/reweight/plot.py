import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

def plot_function(data,clust,system,lays,offset,offset2):
    kT = 0.001987*300
    X = np.unique(data[:,0])
    Y = np.unique(data[:,1])
    dx = round(X[1]-X[0],2)
    dy = round(Y[1]-Y[0],2)
    xmin = -8.0
    xmax = 13.0
    ymin = -6.0
    ymax = 5.0
    XZ = np.arange(xmin,xmax,dx)
    YZ = np.arange(ymin,ymax,dy)
    Z = np.full((len(XZ),len(YZ)),np.amax(data[:,2]))
    for i in range(len(data)):
        x = int((data[i,0]-xmin)/dx)
        y = int((data[i,1]-ymin)/dy)
        Z[x,y] = data[i,2]

    fig, ax = plt.subplots()
    cf = plt.contourf(XZ, YZ, Z.T-np.amax(lays), lays-np.amax(lays))
    #cf = plt.contourf(XZ, YZ, Z.T, 10)
    # set axis and gridlines
    plt.xticks(np.arange(xmin,xmax+1,2),fontsize=16)
    plt.yticks(np.arange(ymin,ymax+1,2),fontsize=16)
    plt.xlabel("LD 1",fontsize=16)
    plt.ylabel("LD 2",fontsize=16)
    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    # add cluster labels                                                                                                                              
    for i in range(len(clust)):
        ax.annotate("S%s" %(int(clust[i,0])), (clust[i,1]+offset[i][0], clust[i,2]+offset[i][1]),fontsize=18,color='r')
        plt.arrow(clust[i,1],clust[i,2],offset2[i][0],offset2[i][1],color='r')
    # set colorbar setting
    cbar = plt.colorbar(cf, ax=ax)
    cbar.set_label('PMF (kcal/mol)', rotation=270, labelpad=18, fontsize=16)
    cbar.ax.tick_params(labelsize=16)
    # save figure
    plt.savefig('%s.pmf.png' %(system))
    plt.savefig('%s.pmf.pdf' %(system))
    plt.close()

clust1 = np.loadtxt("../clusters/rna.centers.dat")
data1 = np.loadtxt("pmf-c2.rna.lda.clust.dat",skiprows=5)
clust2 = np.loadtxt("../clusters/rna_atp.centers.dat")
data2 = np.loadtxt("pmf-c2.rna_atp.lda.clust.dat",skiprows=5)

lays = [0,1,2,3,4,5,6,7,8] # Layers in kcal/mol
offset = ((-5.75,-0.75),(2.75,1.5),(3.25,0.25),(-4.75,0.25))
offset2 = ((-4.0,-0.5),(2.50,1.5),(3.0,0.5),(-3.0,0.5))
plot_function(data1,clust1,"rna",lays,offset,offset2)
plot_function(data2,clust2[1:],"rna_atp",lays,offset[1:],offset2[1:])


