run ../../bin/structure/pymol/color_blind_friendly.py
run ../../bin/structure/pymol/casq2_base.py
run ../../bin/structure/pymol/interface_residues.py
@../../bin/structure/pymol/pub_graphics_base.pml

# So that Yb spheres shine through surfaces. Trying to make spheres really bright. Helps a bit, not a lot. Effect is observable only in ray-traced images.
set spec_reflect, 1
set spec_power, 100

# Used to eliminate shadows in buried areas.
# set two_sided_lighting, on
# set backface_cull, 0

cmd.load("../shared_pdb/filament/output/filament_deo_native.pdb", "filament") 
# "

set cartoon_transparency, 0.5, filament

sele dimer_chains, (chain A or chain B)
sele tetramer_chains, (chain A or chain B or chain C or chain D)
remove polymer and not tetramer_chains
sele all_het, hetatm within 5 of tetramer_chains
remove hetatm and not all_het

# load ../shared_pdb/cavity/output/hollow_deo_native_tetramer_cavity_B.pdb

# Get close to proper orientation. Different rotation than native filament.
rotate y, 90
orient tetramer 
zoom tetramer, -15

set sphere_scale, 1.0, polymer
set sphere_scale, 2.0, elem Yb

apply_standard_colors_tetramer("tetramer", 1)
apply_standard_colors_hetatm()

sele foreground, chain A or chain C 
sele background, chain B or chain D

theme_id = 1
cmd.set("surface_color",chainA_color(theme_id), "chain A and tetramer")
cmd.set("surface_color",chainB_color(theme_id), "chain B and tetramer")
cmd.set("surface_color",chainC_color(theme_id), "chain C and tetramer")
cmd.set("surface_color",chainD_color(theme_id), "chain D and tetramer")

# We may want to keep this and retain the same coloring from figure 1.
myInterfaceResiduesBC = interfaceResidues("tetramer", "(chain B)", "(chain C)", 0.75, "interface_tetramer_BC")
myInterfaceResiduesAD = interfaceResidues("tetramer", "(chain A)", "(chain D)", 0.75, "interface_tetramer_AD")
myInterfaceResiduesAC = interfaceResidues("tetramer", "(chain A)", "(chain C)", 0.75, "interface_tetramer_AC")
myInterfaceResiduesBD = interfaceResidues("tetramer", "(chain B)", "(chain D)", 0.75, "interface_tetramer_BD")

select all_interface_residues, interface_tetramer_BC or interface_tetramer_AD \
     or interface_tetramer_AC or interface_tetramer_BD

orient tetramer 
zoom tetramer, -20

hide everything 


# We may want to keep this and retain the same coloring from figure 1.
# myInterfaceResiduesBC = interfaceResidues("tetramer", "(chain B)", "(chain C)", 0.75, "interface_tetramer_deo_yb_BC")
# myInterfaceResiduesAD = interfaceResidues("tetramer", "(chain A)", "(chain D)", 0.75, "interface_tetramer_deo_yb_AD")
# myInterfaceResiduesAC = interfaceResidues("tetramer", "(chain A)", "(chain C)", 0.75, "interface_tetramer_deo_yb_AC")
# myInterfaceResiduesBD = interfaceResidues("tetramer", "(chain B)", "(chain D)", 0.75, "interface_tetramer_deo_yb_BD")

# select all_interface_residues, interface_tetramer_deo_yb_BC or interface_tetramer_deo_yb_AD \
#      or interface_tetramer_deo_yb_AC or interface_tetramer_deo_yb_BD

# set cartoon_cylindrical_helices, 0

# create_thioredoxin_spheres("ABCD", "deo_yb", "tetramer")

# cmd.set("cartoon_transparency", default_cartoon_transparency())


# sele dimer_het, elem Yb within 4.0 of ((resi 136 or resi 140 or resi 143 or resi 147 or resi 310 or resi 277 or resi 278 or resi 309 or resi 310) and tetramer)

# Breaking this up only for readability.
# sele tetramer_sel1, elem Yb within 4.5 of (resi 184 or resi 144)
# sele tetramer_sel2, elem Yb within 4.5 of (resi 351 or resi 348)

# sele tetramer_het, tetramer_sel1 or tetramer_sel2

# sele tetramer_het_outside, tetramer_het within 4.5 of resi 357

# sele tetramer_het_inside, tetramer_het and not tetramer_het_outside

# sele tetramer_het_thio1, tetramer_het within 4.0 of resi 184

# sele tetramer_het_thio23, tetramer_het and not tetramer_het_thio1

# hide everything

# sele dimer_chains, chain A or chain B

# sele tetramer_chains, chain A or chain B or chain C or chain D

# Now that everything is loaded we can change the camera and the zoom.
# Get close to desired view.
