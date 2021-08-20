import numpy as np
import sys
import MDAnalysis as mda

top_file = sys.argv[1]
traj_file = sys.argv[2]
out_file = sys.argv[3]

u=mda.Universe(top_file,traj_file)


#sel = [u.select_atoms("resid 540 and (name H or name O or name OE1 or name OE2)"),u.select_atoms("resid 539 and (name H or name O or name HG)"),u.select_atoms("resid 538 and (name H or name O)"),u.select_atoms("resid 537 and (name H or name O or name OE1 or name HE 21 or name HE22)"),u.select_atoms("resid 536 and (name H or name O or name HG)"),u.select_atoms("resid 535 and (name H or name O or name HG)"),u.select_atoms("resid 534 and (name H or name O or name OD1 or name OD2)"),u.select_atoms("resid 533 and (name H or name O)")]

sel = [u.select_atoms("resid 540"),u.select_atoms("resid 539"),u.select_atoms("resid 538"),u.select_atoms("resid 537"),u.select_atoms("resid 536"),u.select_atoms("resid 535"),u.select_atoms("resid 534"),u.select_atoms("resid 533")]

pSel = u.select_atoms("(resname U or resname U3 or resname U5) and name P")
aSel = u.select_atoms("resname ATP or resname MG")

outa = open("%s.atp.dat" %(out_file),'w')
outb = open("%s.rna.dat" %(out_file),'w')
out2 = open("%s.phosphate.dat" %(out_file),'w')
for ts in u.trajectory:
    for s in sel:
        dist1 = 1000
        ind1 = 0
        dist2 = 1000
        for atom in s.atoms:
            for atom2 in pSel.atoms:
                d = np.linalg.norm(atom.position-atom2.position)
                if d < dist1:
                    dist1 = d
                    ind1 = atom2.resid
            for atom2 in aSel.atoms:
                d = np.linalg.norm(atom.position-atom2.position)
                if d < dist2:
                    dist2 = d
        outa.write("  %12.8f" %(dist1))
        out2.write("  %3i" %(ind1))
        outb.write("  %12.8f" %(dist2))
    outa.write("\n")
    outb.write("\n")
    out2.write("\n")
out.close
out2.close

