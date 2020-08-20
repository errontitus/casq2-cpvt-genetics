@shared_make_figure_dimer_yb_overview.pml

# rotate y, 45
# # translate the copy of the ligands away from the camera
# translate [0,0,-3], yb_copy
# cmd.set("surface_color", chainB_color(1), "chain B")
# show surface, chain B
# disable yb_copy

# # orient dimer

# extract obj_chain_A, chain A
# extract obj_chain_B, chain B

set sphere_scale, 1.0, elem Yb
set sphere_scale, 1.5, polymer
set cartoon_transparency, 0.5, dimer_yb

# cmd.set("cartoon_transparency", default_cartoon_transparency(), "dimer_deo_native")
# show cartoon, dimer 

apply_standard_colors_dimer_spheres("dimer_yb", 1)

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
show spheres, (resi 308 or resi 310) and dimer_yb
save_image_dimer("packing_mutants_P308L_overview")
# turn x, 90
# save_image_dimer("packing_mutants_P308L_overview_90")


# 
# Tetramer disease mutations 
#
# S173I
# K180R
# D325E
# E39K


