@shared_make_figure_dimer_yb_closeup.pml

sele P308_helix, (resi 308 or resi 309 or resi 310) and dimer_yb
# sele R251_D310_native, (resi 251 or resi 276 or resi 310) and dimer_native

sele yb_310, elem yb within 3.5 of (dimer_yb and resi 310)

#sele SO4_251, chain I within 8 of ((dimer_yb and chain A and resi 251) or (dimer_yb and chain B and resi 251))

#sele SO4_251_native, (resn SO4 and dimer_native) within 6 of ((dimer_native and chain A and resi 251) or (dimer_native and chain B and resi 251))

hide everything

# SO4
# distance (dimer_yb and (chain A) and i. 251 and n;NH1), (dimer_yb and SO4_251 and i. 4 and n;O2)
# distance (dimer_yb and (chain B) and i. 251 and n;NH2), (dimer_yb and SO4_251 and i. 4 and n;O3)
# distance (dimer_yb and (chain Y) and yb_310), (dimer_yb and SO4_251 and i. 4 and n;O2)
# distance (dimer_yb and (chain B) and i. 276 and n;NZ), (dimer_yb and SO4_251 and i. 4 and n;O4)


# distance (dimer_yb and (chain A) and i. 310 and n;OD1), (dimer_yb and (chain Y) and yb_310)
distance (dimer_yb and (chain B) and i. 310 and n;OD1), (dimer_yb and yb_310)

hide labels

show cartoon, dimer_yb
#side_chain_helper("P308_helix and chain A")
side_chain_helper("P308_helix and resi 310")
#show sticks, (resi 308 and chain A and dimer_yb) and not (name c,o)
show sticks, (resi 308 and dimer_yb) and not (name c,o)
show spheres, yb_310
cartoon oval, resi 308-310
#show sticks, SO4_251

# turn y, -90
select view_center, yb_310 
# P308_helix and chain A
hide cartoon, resi 245-255
turn y, 55
zoom view_center, 9

# 
save_image_dimer("packing_mutants_P308L_closeup")

# hide dashes

# isomesh yb_mesh, yb_map, 1.5, dimer_yb, carve=2.5
# color blue, yb_mesh
# show mesh, yb_mesh
# save_image_closeup("dimer_interface_D310_closeup_yb_map")

# hide everything, yb_mesh
# isomesh yb_mesh_anom, yb_map_anom, 3, dimer_yb, carve=3
# color red, yb_mesh_anom
# show mesh, yb_mesh_anom
# save_image_closeup("dimer_interface_D310_closeup_yb_map_anom")

# hide everything 
# isomesh native_mesh, native_map, 1.5, R251_D310_native or SO4_251_native, carve=2
# color blue, native_mesh
# show mesh, native_mesh
# show cartoon, dimer_native
# show sticks, SO4_251_native
# side_chain_helper("R251_D310_native")
# save_image_closeup("dimer_interface_D310_closeup_native_map")


bg_color white

