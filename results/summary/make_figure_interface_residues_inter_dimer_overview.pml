@shared_make_figure_interface_residues.pml

apply_standard_colors_tetramer_spheres("tetramer", 1)

# myInterfaceResiduesAB = interfaceResidues("tetramer", "(chain A)", "(chain B)", 0.75, "interface_dimer_AB")

# myInterfaceResiduesCD = interfaceResidues("tetramer", "(chain C)", "(chain D)", 0.75, "interface_dimer_CD")

show cartoon, tetramer

set sphere_scale, 1.5, polymer

hide spheres, all
# color yellow, all_interface_residues

# inter dimer
# % S173I (Ph+ Het, inter dimer)
# % K180R (Ph+ Het, inter dimer)
# % D325E (Ph+ Het, inter dimer)
# show spheres, all_interface_residues and (resi 173 or resi 180 or resi 325)

show spheres, all_interface_residues 
# and (resi 173 or resi 180 or resi 325)

# Not shown (either VUS, redundant, or like Y55C discussed separately):
# % E39K Ph- Het, unknown mechanism(s)
# % Y55C (Ph+ Het, packing)
# % K206N (Ph+ Het, unknown)
# % P231S Ph- Het, unknown mechanism(s)
# % R250C Ph- Het, unknown mechanism(s)
# % P308Q (Ph+ Het, packing)
# % W361R (Ph+ Het, unknown)
# % L366P Ph- Het, unknown mechanism(s)

save_image_tetramer("interface_residues_inter_dimer_overview")

