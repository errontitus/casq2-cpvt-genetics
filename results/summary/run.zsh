#! /bin/zsh
#

mkdir -p output
rm output/*

pymol -cq make_surface_residue_list.pml

pdb_gap ../data/structures/6OWV_native.pdb

pymol -cq make_figure_hydrophobic_core_overview.pml
pymol -cq make_figure_interface_residues_inter_dimer_overview.pml
pymol -cq make_figure_interface_residues_packing_variants_overview.pml
pymol -cq make_figure_interface_residues_intra_dimer_overview.pml

python make_interface_residue_lists.py
pymol -cq make_surface_residue_list.pml

alias crop="python ../../bin/utils/crop_to_bounding_box.py"
# Refresh the alias
source ~/.zshrc

crop ./output/interface_residues_inter_dimer_overview.png
crop ./output/interface_residues_packing_overview.png
crop ./output/interface_residues_intra_dimer_overview.png

crop ./output/hydrophobic_core_overview.png