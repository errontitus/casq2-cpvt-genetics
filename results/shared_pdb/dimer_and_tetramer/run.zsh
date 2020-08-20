#! /bin/zsh
#

mkdir -p output
rm output/*

# It's important to save the tetramers in separate PDB files.
# If you try to do everything in one PyMOL session, PyMOL will consider the chains independently movable.

# Our native structure. 
pymol -cq ../../../data/structures/6OWV_native.pdb make_dimer_and_tetramer_deo_native.pml

# Our yb-soaked structure.
# pymol -cq ../../../data/structures/6OWW_yb.pdb make_only_tetramer_deo_yb.pml

# # Our yb-soaked structure - multiple different dimers.
# pymol -cq ../../../data/structures/6OWW_yb.pdb make_only_dimer_deo_yb.pml
