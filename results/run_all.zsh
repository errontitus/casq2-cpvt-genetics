#! /bin/zsh
#

source clean.zsh

cd ./shared_pdb
# Builds the common/shared result objects in the required order.
source run.zsh
cd ..

cd ./assembly_kinetics
source run.zsh
cd ..

cd ./interface_mutants
source run.zsh
cd ..

cd ./materials_and_methods
source run.zsh
cd ..

cd ./packing_mutants
source run.zsh
cd ..

cd ./SEC
source run.zsh
cd ..

cd ./shared_pdb
source run.zsh
cd ..

cd ./summary
source run.zsh
cd ..