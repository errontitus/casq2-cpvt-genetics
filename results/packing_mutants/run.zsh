#! /bin/zsh
#

mkdir -p output

rm output/*

# These views use the native structure.
pymol -cq make_figure_packing_mutants_Y55C_R251H_overview.pml
pymol -cq make_figure_packing_mutants_Y55C_closeup.pml
pymol -cq make_figure_packing_mutants_R251H_closeup.pml

# These views use the Yb structure.
pymol -cq make_figure_packing_mutants_P308L_overview.pml
pymol -cq make_figure_packing_mutants_P308L_closeup.pml

alias crop="python ../../bin/utils/crop_to_bounding_box.py"
# Refresh the alias
source ~/.zshrc

crop ./output/packing_mutants_Y55C_overview.png
crop ./output/packing_mutants_Y55C_closeup.png

crop ./output/packing_mutants_R251H_overview.png
crop ./output/packing_mutants_R251H_closeup.png

crop ./output/packing_mutants_P308L_overview.png
crop ./output/packing_mutants_P308L_closeup.png