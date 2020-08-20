#! /bin/zsh
#

mkdir -p output

rm output/*

pymol -cq make_figure_interface_mutants_S173_K180_D325_overview.pml
pymol -cq make_figure_interface_mutants_S173_D325_closeup.pml
pymol -cq make_figure_interface_mutants_K180R_closeup.pml

pymol -cq make_figure_packing_mutant_hypothesis.pml

alias crop="python ../../bin/utils/crop_to_bounding_box.py"
# Refresh the alias
source ~/.zshrc

crop ./output/interface_mutants_S173_D325_overview.png
crop ./output/interface_mutants_S173_D325_closeup.png

crop ./output/interface_mutants_K180_overview_90.png
crop ./output/interface_mutants_K180_closeup.png

crop ./output/packing_mutant_hypothesis.png
crop ./output/packing_mutant_hypothesis_90.png
