import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as md
import sys

prmtop = sys.argv[1]
traj = sys.argv[2]
outfile = sys.argv[3]

u = md.Universe(prmtop,traj)

rSels = [u.select_atoms("resid 516 and name CA"),u.select_atoms("resid 311 and name CA")]
pSels = u.select_atoms("(resname U or resname U3 or resname U5) and name P")
nSel = len(rSels)
out = open("%s.distances.dat" %(outfile),'w')
out2 = open("%s.dist_list.dat" %(outfile),'w')
out3 = open("%s.phosphate.dat" %(outfile),'w')
for ts in u.trajectory:
    if ts.frame == 0:
        for i in range(len(rSels)):
            atom = rSels[i].atoms[0]
            out2.write("  %3s %3i %3s %3s %3s %3s\n" %(atom.resname,atom.resid,atom.name,"RNA","XXX","P"))   
            for j in range(i+1,len(rSels)):
                atom2 = rSels[j].atoms[0]
                out2.write("  %3s %3i %3s %3s %3s %3s\n" %(atom.resname,atom.resid,atom.name,atom2.resname,atom2.resid,atom2.name))   
        out2.close
        
    for i in range(len(rSels)):
        rAtom = rSels[i].atoms[0]
        dist = 1000
	p_sel = 0
        for pAtom in pSels.atoms:
            d = np.linalg.norm(rAtom.position-pAtom.position)
            if d < dist:
                dist = d
		p_sel = pAtom.resid
        out3.write("  %3i" %(p_sel))
        out.write("  %12.8f" %(dist))
        for j in range(i+1,len(rSels)):
            dist = np.linalg.norm(rAtom.position-rSels[j].atoms[0].position)
            out.write("  %12.8f" %(dist))
    out.write("\n")
    out3.write("\n")

        
            

