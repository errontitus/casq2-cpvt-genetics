#! /bin/zsh
#

mkdir -p output
rm output/*

# cp ../filament_hollow/output/*.pdb ./output

pdb_native=../../../data/structures/6OWV_native.pdb
pymol -cq $pdb_native make_filament_deo_native.pml
