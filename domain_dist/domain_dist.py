import numpy as np
import sys
import MDAnalysis as mda

def distance(pos1,pos2):
    dx = pos1 - pos2
    dis = np.sqrt(np.dot(dx,dx))
    return dis

top_file = sys.argv[1]
traj_file = sys.argv[2]
out_file = sys.argv[3]
u = mda.Universe(top_file,traj_file)


sel1 = u.select_atoms("resid 152:160 or resid 162:168 or resid 181:189 or resid 191:202 or resid 208:214 or resid 222:228")
sel2 = u.select_atoms("resid 276:281 or resid 304:309 or resid 330:333 or resid 355:360 or resid 366:374 or resid 392:400")
sel3 = u.select_atoms("resid 510:514 or resid 541:549 or resid 569:577")

nFrames = len(u.trajectory)
dist = np.zeros((nFrames,3),dtype=float)

out1 = open("%s.1A-1B.dat" %(out_file),'w')
out2 = open("%s.2A-1B.dat" %(out_file),'w')
out3 = open("%s.1A-2A.dat" %(out_file),'w')
out4 = open("%s.all.dat" %(out_file),'w')
for ts in u.trajectory:
    com1 = sel1.atoms.center_of_mass()
    com2 = sel2.atoms.center_of_mass()
    com3 = sel3.atoms.center_of_mass()
    
    dist[ts.frame,0] = distance(com1,com2)
    dist[ts.frame,1] = distance(com1,com3)
    dist[ts.frame,2] = distance(com2,com3)

    out1.write("  %10.5f\n" %(dist[ts.frame,0]))
    out2.write("  %10.5f\n" %(dist[ts.frame,1]))
    out3.write("  %10.5f\n" %(dist[ts.frame,2]))
    out4.write("  %10.5f  %10.5f  %10.5f\n" %(dist[ts.frame,0],dist[ts.frame,1],dist[ts.frame,2]))

out1.close
out2.close
out3.close
out4.close
