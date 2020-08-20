#! /bin/zsh
#

mkdir -p output
rm output/*

# To generate a config file. Edited by hand to modify output folder, no other changes.
# pisa -cfg-template > pisa.cfg

# PISA analysis of our structure.
pisa tetramer_deo_native -analyse ../dimer_and_tetramer/output/tetramer_deo_native_no_het.pdb ./pisa.cfg

# pisa tetramer_deo_native -list interfaces ./pisa.cfg 

pisa tetramer_deo_native -xml interfaces ./pisa.cfg > ./output/tetramer_deo_native_no_het_pisa.xml

# Monomer
# pisa monomer_deo_native -analyse ../monomer/output/monomer_deo_native_no_het.pdb ./pisa.cfg

# pisa monomer_deo_native -xml monomers ./pisa.cfg > ./output/monomer_deo_native_no_het_pisa.xml

