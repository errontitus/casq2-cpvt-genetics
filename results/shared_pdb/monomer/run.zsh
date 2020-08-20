#! /bin/zsh
#

mkdir -p output
rm output/*

# Our native structure. 
pymol -cq ../../../data/structures/6OWV_native.pdb make_monomer_deo_native.pml
