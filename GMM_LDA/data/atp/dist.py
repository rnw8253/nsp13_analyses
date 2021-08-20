import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as md
import sys

prmtop = sys.argv[1]
traj = sys.argv[2]
outfile = sys.argv[3]

u = md.Universe(prmtop,traj)

dist_list = [["281","311"],["281","534"],["311","534"],["516","534"],["534","567"]]
pSels = u.select_atoms("(resname U or resname U3 or resname U5) and name P")
rSels = [u.select_atoms("resid 534 and name CA")]

dSels = []
for dist in dist_list:
    temp = []
    temp.append(u.select_atoms("resid %s and name CA" %(dist[0])))
    temp.append(u.select_atoms("resid %s and name CA" %(dist[1])))
    dSels.append(temp)		      

out = open("%s.distances.dat" %(outfile),'w')
out2 = open("%s.dist_list.dat" %(outfile),'w')
out3 = open("%s.phosphate.dat" %(outfile),'w')
for ts in u.trajectory:
    if ts.frame == 0:
        for i in range(len(dSels)):
            atom = dSels[i][0].atoms[0]
	    atom2 = dSels[i][1].atoms[0]
	    out2.write("  %3s %3i %3s %3s %3s %3s\n" %(atom.resname,atom.resid,atom.name,atom2.resname,atom2.resid,atom2.name))   
        for i in range(len(rSels)):
	    atom = rSels[i].atoms[0]
	    out2.write("  %3s %3i %3s ssRNA XXX P\n" %(atom.resname,atom.resid,atom.name))   	    
        out2.close
   	
    for i in range(len(dSels)):
        atom = dSels[i][0].atoms[0]
        atom2 = dSels[i][1].atoms[0]
	dist = np.linalg.norm(atom.position-atom2.position)
        out.write("  %12.8f" %(dist))	

    for i in range(len(rSels)):
       atom = rSels[i].atoms[0]
       dist = 1000
       p_sel = 0
       for pAtom in pSels.atoms:
       	   d = np.linalg.norm(atom.position-pAtom.position)
           if d < dist:
              dist = d
              p_sel = pAtom.resid
       out3.write("  %3i" %(p_sel))
       out.write("  %12.8f" %(dist))
    out.write("\n")
    out3.write("\n")


