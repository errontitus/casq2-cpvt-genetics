@shared_make_figure_interface_residues.pml

remove not dimer_chains

apply_standard_colors_dimer_spheres("dimer_chains", 1)

orient dimer_chains 
zoom dimer_chains, 5

set sphere_scale, 1.5, polymer

hide everything 

# inter dimer packing 
# % R251H packing
# % P308L (Ph+ Het, packing)
sele packing_variants, resi 308 or resi 251
color red, packing_variants
show spheres, packing_variants

show cartoon, dimer_chains

save_image_dimer("interface_residues_packing_overview")
