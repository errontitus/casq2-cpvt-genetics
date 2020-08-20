@shared_make_figure_dimer.pml
@../../bin/structure/pymol/pub_graphics_ligands_and_bonds.pml

set sphere_scale, 0.4, elem Yb

# sele dimer_chains, (chain A or chain B) and polymer

# select_dimer_yb("dimer_het", "dimer_yb")
# select_dimer_yb_residues("dimer_het_residues", "dimer_yb")

# Now that everything is loaded we can change the camera and the zoom.
# rotate x, -45
# rotate y, 180
orient dimer_yb_polymer 
zoom dimer_yb_polymer
# turn x, 180