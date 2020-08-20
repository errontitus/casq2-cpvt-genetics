run ../../bin/structure/pymol/color_blind_friendly.py
run ../../bin/structure/pymol/casq2_base.py
run ../../bin/structure/pymol/find_surface_residues.py
@../../bin/structure/pymol/pub_graphics_base.pml

cmd.load("../shared_pdb/monomer/output/monomer_deo_native_no_het.pdb", "monomer") 
# "

python 

import numpy as np

is_solvent_residue = [0] * 400
Accessible = np.array(is_solvent_residue)

residues = findSurfaceResidues(cutoff=4)

output = ""
for i, (chain, seq_num) in enumerate(residues):
    index = int(seq_num)
    Accessible[index] = 1

print Accessible

tex =""
for i in range(23,372,1):
    if i in range(58,69):
        print "skip"
    elif i in range(259,268):
        print "skip"
    elif Accessible[i] == 1:
        tex = "\\feature{top}{1}{" + str(i) + ".." + str(i) + "}{---[\colorSolventExposed]}{}\n"
    else:
        tex = "\\feature{ttop}{1}{" + str(i) + ".." + str(i) + "}{---[\colorHydrophobicCore]}{}\n"
    print tex 
    output = output + tex


# residue_list = list(range(0, 400)) 
# Accessible = np.array(list(zip(residue_list,is_solvent_residue)))
# columns =['seq_num', 'is_solvent_residue'])

# tex =""
# for i in range(23,371,1):
#     if Accessible["is_solvent_residue"] == 1:
#         tex = "\\feature{top}{1}{" + str(seq_num) + ".." + str(seq_num) + "}{---[\colorSolventExposed]}{}\n"
#     else:
#         tex = "\\feature{top}{1}{" + str(seq_num) + ".." + str(seq_num) + "}{---[\colorHydrophobicCore]}{}\n"
#     print tex 
#     output = output + tex

import sys 

out_file = "./output/surface_residues_texshade.tex"
with open(out_file, "wb") as f:
    f.write(output)

python end
