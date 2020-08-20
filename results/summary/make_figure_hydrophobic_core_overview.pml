@shared_make_figure_interface_residues.pml

run ../../bin/structure/pymol/find_surface_residues.py

orient dimer_chains 
zoom dimer_chains, 5

remove not chain A
residues = findSurfaceResidues(cutoff=4)

color ruby, not exposed_res_01

set surface_color, slate, chain A
set transparency, 0.5

# color blue, exposed_res_01

# remove not dimer_chains

# apply_standard_colors_dimer_spheres("dimer_chains", 1)

# myInterfaceResiduesAB = interfaceResidues("dimer_chains", "(chain A)", "(chain B)", 0.75, "interface_dimer_AB")


hide everything 

# Maybe show these (green) if not too busy?
# C53F core
# L77P core
# L167H core
# F182S core
# P191L core
# I270T core

sele hydrophobes, resi 53 or resi 77 or resi 167 or resi 182 or resi 191 or resi 270
# color green, hydrophobes and chain A
# show spheres, hydrophobes and chain A

show spheres, not exposed_res_01
show surface, chain A

# show cartoon, dimer_chains and chain A
bg_color white

save_image_dimer("hydrophobic_core_overview")
