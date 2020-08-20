run ../../bin/structure/pymol/color_blind_friendly.py
run ../../bin/structure/pymol/casq2_base.py
@../../bin/structure/pymol/pub_graphics_base.pml
run ../../bin/structure/pymol/color_by_rmsd.py

# remove not dimer_chains

load ../../data/structures/1sji.ent, 1sji
load ../shared_pdb/dimer_and_tetramer/output/dimer_deo_native.pdb, native_dimer
load ../shared_pdb/dimer_and_tetramer/output/dimer_deo_native.pdb, native_dimer_1
load ../shared_pdb/dimer_and_tetramer/output/dimer_deo_native.pdb, native_dimer_2

remove hetatm

orient native_dimer 
zoom native_dimer, 5

align 1sji, native_dimer
align native_dimer_1 and chain A, 1sji and chain A
align native_dimer_2 and chain B, 1sji and chain B

colorbyrmsd native_dimer_1 and chain A, native_dimer and chain A, doAlign=0
colorbyrmsd native_dimer_2 and chain B, native_dimer and chain B, doAlign=0

rotate x, 180
orient native_dimer 
zoom native_dimer, 5

hide everything 
set cartoon_transparency, 0.5, native_dimer
color gray50, native_dimer
show cartoon, native_dimer
show cartoon, (native_dimer_1 and chain A) or (native_dimer_2 and chain B)

save_image_dimer("packing_mutant_hypothesis")

turn y, 90
save_image_dimer("packing_mutant_hypothesis_90")
