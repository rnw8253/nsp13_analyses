
import numpy as np
import MDAnalysis as md

prmtop = "stripped.nsp13_cov_2_apo.solv.prmtop"
dcd = "nsp13_cov_2_apo.solv.prod.002.stripped.dcd"
out = open("apo_length.dat",'w')
coord = md.Universe(prmtop,dcd)
selection = coord.select_atoms("protein")
extent = np.empty(coord.trajectory.n_frames,dtype=np.float64)
for ts in coord.trajectory:
    selection.translate(-selection.center_of_mass())
    covar = np.dot(selection.positions.T,selection.positions)
    e, v = np.linalg.eigh(covar)
    principleAxisProjection = np.dot(selection.positions,v[:,2])
    extent[ts.frame-1] = np.amax(principleAxisProjection) - np.amin(principleAxisProjection)

out.write("Average extent: %s", np.mean(extent))
out.write("Standard deviation of extent: %s", np.std(extent))
out.write("Standard error of extent: %s", np.std(extent)/np.sqrt(coord.trajectory.n_frames))

