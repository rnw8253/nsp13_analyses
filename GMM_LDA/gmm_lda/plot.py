import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

def plot_function(data,clust,system):
    x = data[:,0]
    y = data[:,1]
    xmin = -6.0
    xmax = 12.0
    ymin = -6.0
    ymax = 5.0
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=100, range=[[xmin,xmax],[ymin,ymax]], density=True)
    heatmap = -0.6*np.log(heatmap)    
    heatmap -= np.amin(heatmap)
    fig, ax = plt.subplots()
    #cf = plt.contourf(xedges[1:], yedges[1:], heatmap.T, 10)
    cf = plt.contourf(xedges[1:], yedges[1:], heatmap.T, [0,0.6,1.2,1.8,2.4,3.0,3.6,4.2,4.8])
    # set axis and gridlines
    plt.xticks(np.arange(xmin,xmax+1,2),fontsize=16)
    plt.yticks(np.arange(ymin,ymax+1,2),fontsize=16)
    plt.xlabel("LD 1",fontsize=16)
    plt.ylabel("LD 2",fontsize=16)
    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    # add cluster labels
    offset = ((-4.5,-0.75),(2.75,1.5),(3.25,0.25),(-3.5,0.25))
    offset2 = ((-3.5,-0.5),(2.50,1.5),(3.0,0.5),(-2.50,0.5))
    for i in range(len(clust)):
        ax.annotate(i+1, (clust[i,1]+offset[i][0], clust[i,2]+offset[i][1]),fontsize=18,color='r')        
        plt.arrow(clust[i,1],clust[i,2],offset2[i][0],offset2[i][1],color='r')
    # set colorbar setting
    cbar = plt.colorbar(cf, ax=ax)
    cbar.set_label('PMF (kcal/mol)', rotation=270, labelpad=18, fontsize=16)
    cbar.ax.tick_params(labelsize=16)
    # save figure
    plt.savefig('%s.pmf.png' %(system))
    plt.savefig('%s.pmf.pdf' %(system))
    plt.close()


clust = np.loadtxt("cluster_centers.dat")
data = np.loadtxt("lda.dat",skiprows=5)


plot_function(data,clust,"combined")
plot_function(data[:1199794],clust,"rna")
plot_function(data[1199794:],clust,"rna_atp")


