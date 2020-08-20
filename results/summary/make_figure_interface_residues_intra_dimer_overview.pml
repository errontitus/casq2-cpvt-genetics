@shared_make_figure_interface_residues.pml

remove not dimer_chains

apply_standard_colors_dimer_spheres("dimer_chains", 1)

myInterfaceResiduesAB = interfaceResidues("dimer_chains", "(chain A)", "(chain B)", 0.75, "interface_dimer_AB")

orient dimer_chains 
zoom dimer_chains, 5

set sphere_scale, 1.5, polymer

hide everything 

# R33Q (recessive, dimer interface)
# D307H (recessive, dimer interface)
# D310N (recessive, dimer interface)
# color magenta, interface_dimer_AB or (resi 33 or resi 307 or resi 310)
#show spheres, (resi 33 or resi 307 or resi 310)

show spheres, interface_dimer_AB

# Maybe show these (green) if not too busy?
# C53F core
# L77P core
# L167H core
# F182S core
# P191L core
# I270T core
#sele hydrophobes, resi 53 or resi 77 or resi 167 or resi 182 or resi 191 or resi 270
#color green, hydrophobes
#show spheres, hydrophobes

show cartoon, dimer_chains

save_image_dimer("interface_residues_intra_dimer_overview")
