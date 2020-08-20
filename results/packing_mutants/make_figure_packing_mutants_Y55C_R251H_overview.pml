@shared_make_figure_dimer_native_overview.pml

# rotate y, 45
# # translate the copy of the ligands away from the camera
# translate [0,0,-3], yb_copy
# cmd.set("surface_color", chainB_color(1), "chain B")
# show surface, chain B
# disable yb_copy

# # orient dimer

# extract obj_chain_A, chain A
# extract obj_chain_B, chain B

# set sphere_scale, 1.0, elem Yb
set sphere_scale, 1.5, polymer
set cartoon_transparency, 0.5, dimer_native

# cmd.set("cartoon_transparency", default_cartoon_transparency(), "dimer_deo_native")
# show cartoon, dimer 

apply_standard_colors_dimer_spheres("dimer_native", 1)

# 
# Dimer disease mutations 
#
# R33Q
# K206N
# R251H
# D307H
# P308L
# orient dimer
# rotate y, 25
hide spheres, all
show spheres, (resi 251 or resi 276) and dimer_native
save_image_dimer("packing_mutants_R251H_overview")

hide spheres, all
show spheres, (resi 55) and dimer_native
save_image_dimer("packing_mutants_Y55C_overview")

# hide spheres, all
# show surface, dimer_native
# set surface_color, blue, (resi 55) and chain B and dimer_native
# save_image_dimer("packing_mutants_Y55C_overview_surface")

# 
# Tetramer disease mutations 
#
# S173I
# K180R
# D325E
# E39K


