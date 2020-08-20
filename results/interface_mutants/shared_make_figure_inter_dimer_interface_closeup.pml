run ../../bin/structure/pymol/color_blind_friendly.py
run ../../bin/structure/pymol/casq2_base.py
run ../../bin/structure/pymol/interface_residues.py
@../../bin/structure/pymol/pub_graphics_base.pml
@../../bin/structure/pymol/pub_graphics_ligands_and_bonds.pml

# So that Yb spheres shine through surfaces. Trying to make spheres really bright. Helps a bit, not a lot. Effect is observable only in ray-traced images.
set spec_reflect, 1
set spec_power, 100

# Used to eliminate shadows in buried areas.
# set two_sided_lighting, on
# set backface_cull, 0

# cmd.load("../shared_pdb/filament/output/filament_deo_native.pdb", "filament") 
# # "

# sele tetramer_chains, (chain A or chain B or chain C or chain D)
# remove polymer and not tetramer_chains
# sele all_het, hetatm within 5 of tetramer_chains
# remove hetatm and not all_het

# # Get close to desired orientation.
# rotate y, 90

# Our new way of loading the structure more amenable to showing maps:
# set normalize_ccp4_maps, on
# load ./output/6OWV_native_refined_map_coefficients_2mFo-DFc.ccp4, native_map
load ../../data/structures/6OWV_native.pdb, tetramer_deo_native
symexp N, tetramer_deo_native, tetramer_deo_native, 3
# You clicked /N07000000//A/ALA`204/CA
alter N01000000, chain='B'
alter N06000000, chain='C'
alter tetramer_deo_native, chain='D'
# We need an object
extract tetramer_native, N07000000 or N01000000 or N06000000 or tetramer_deo_native
remove tetramer_deo_native
remove N*

# No object movements; keep map consistent with model.
turn y, 180
turn x, 180
orient tetramer_native 
zoom tetramer_native, -20

cmd.set("cartoon_transparency", default_cartoon_transparency())

apply_standard_colors_tetramer("tetramer_native", 1)
apply_standard_colors_hetatm()

# sele tetramer_chains, chain A or chain B or chain C or chain D

# select_tetramer_yb_thio23_only("tetramer_het_thio23", "chain B or chain C", "chain A or chain D")
# select_tetramer_yb_residues_thio23_only("tetramer_het_residues_thio23", "chain B or chain C", "chain A or chain D")

# select_tetramer_yb("tetramer_het_all", "chain B or chain C", "chain A or chain D")
# select_tetramer_yb_residues("tetramer_het_residues_all", "chain B or chain C", "chain A or chain D")

# set sphere_scale, , polymer
# set sphere_scale, 0.4, elem Yb

hide everything