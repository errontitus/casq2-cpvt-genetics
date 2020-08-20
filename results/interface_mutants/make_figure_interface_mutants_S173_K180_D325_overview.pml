@shared_make_figure_inter_dimer_interface.pml

apply_standard_colors_tetramer_spheres("tetramer", 1)

show cartoon, tetramer

set sphere_scale, 1.5, polymer
set cartoon_transparency, 0.5, tetramer

# Preferred option: show all pertinent interface residues as spheres and then
# box them separately for closeups. But it turns out they are all too close to each other, so you can't distinguish them.
# show spheres, (resi 325 or resi 180 or resi 173) and all_interface_residues

hide spheres, all
show spheres, (resi 325 or resi 173 or resi 319 or resi 87) and all_interface_residues
save_image_tetramer("interface_mutants_S173_D325_overview")

turn x, 90
hide spheres, all
show spheres, (resi 180 or resi 50) and all_interface_residues
save_image_tetramer("interface_mutants_K180_overview_90")
