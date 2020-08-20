#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et
import pandas as pd

class pisa_xml_to_dataframe:

    def __init__(self, filename):
        # self.root = ET.XML(xml_data)
        self.root = et.parse(filename).getroot()

    def _parse_interfaces(self, root):
        cols = ['ID', 'Monomer1', 'Monomer2', 'Area', 'Pvalue', 'DeltaG', 'Nhb', 'Nsb', 'Nds']
        interfaces = pd.DataFrame(columns=cols)
        for interface in root.findall('interface'):
            id = interface.find("id").text
            int_area = str(round(float(interface.find("int_area").text),0))
            int_solv_en = str(round(float(interface.find("int_solv_en").text),1))
            pvalue = interface.find("pvalue").text

            h_bonds = interface.find("h-bonds")
            n_h_bonds = h_bonds.find("n_bonds").text

            salt_bridges = interface.find("salt-bridges")
            n_salt_bridges = salt_bridges.find("n_bonds").text

            ss_bonds = interface.find("ss-bonds")
            n_ss_bonds = ss_bonds.find("n_bonds").text

            for molecule in interface.findall('molecule'):
                mol_id = molecule.find("id").text
                if mol_id == "1":
                    mol1 = molecule.find("chain_id").text
                if mol_id == "2":
                    mol2 = molecule.find("chain_id").text

            # print id, mol1, mol2, int_area, int_solv_en, pvalue, n_h_bonds, n_salt_bridges, n_ss_bonds
            interfaces = interfaces.append(
                    pd.Series([id, mol1, mol2, int_area, pvalue, int_solv_en,
                              n_h_bonds, n_salt_bridges, n_ss_bonds], index=cols),
                             ignore_index=True)
        return interfaces

    def _parse_buried_residues(self, root, chain1, chain2):
        cols = ['chain1', 'chain2', 'name', 'seq_num', 'asa', 'bsa', 'is_interface_residue']
        buried_residues = pd.DataFrame(columns=cols)
        for interface in root.findall('interface'):
            for molecule in interface.findall('molecule'):
                mol_id = molecule.find("id").text
                if mol_id == "1":
                    mol1 = molecule.find("chain_id").text
                if mol_id == "2":
                    mol2 = molecule.find("chain_id").text

            print mol1 
            print mol2
            print " "
            is_interface_residue = 1
            if mol1 == chain1 and mol2 == chain2:
                for molecule in interface.findall('molecule'):
                    for residues in molecule.findall("residues"):
                        for residue in residues.findall("residue"):
                            asa = str(residue.find("asa").text)
                            bsa = str(residue.find("bsa").text)
                            seq_num = str(residue.find("seq_num").text)
                            name = residue.find("name").text

                            # print id, mol1, mol2, int_area, int_solv_en, pvalue, n_h_bonds, n_salt_bridges, n_ss_bonds
                            if float(bsa) > 0:
                                buried_residues = buried_residues.append(
                                        pd.Series([chain1, chain2, name, seq_num, asa, bsa, is_interface_residue], index=cols),
                                                ignore_index=True)

        return buried_residues

    # Fully recursive parser. Hot helpful here.
    #    def parse_root(self, root):
    #        return [self.parse_element(child) for child in iter(root)]
    #
    #    def parse_element(self, element, parsed=None):
    #        if parsed is None:
    #            parsed = dict()
    #        for key in element.keys():
    #            parsed[key] = element.attrib.get(key)
    #        if element.text:
    #            parsed[element.tag] = element.text
    #        for child in list(element):
    #            self.parse_element(child, parsed)
    #        return parsed

    def get_interfaces(self):
        return self._parse_interfaces(self.root)

    def get_buried_residues(self, chain1, chain2):
        return self._parse_buried_residues(self.root, chain1, chain2)

################

base_path = "../shared_pdb/pisa/output/"
pdb = "tetramer_deo_native"

# Dimer
xml2df = pisa_xml_to_dataframe(base_path + pdb + "_no_het_pisa.xml")
dfAB = xml2df.get_buried_residues("A","B")
print "AB"

# Dimer-Dimer inside
xml2df = pisa_xml_to_dataframe(base_path + pdb + "_no_het_pisa.xml")
dfBC = xml2df.get_buried_residues("B","C")
print "BC"

# Dimer-Dimer outside-inside
xml2df = pisa_xml_to_dataframe(base_path + pdb + "_no_het_pisa.xml")
dfAC = xml2df.get_buried_residues("A","C")
print "AC"

# Dimer-Dimer inside-outside
xml2df = pisa_xml_to_dataframe(base_path + pdb + "_no_het_pisa.xml")
dfBD = xml2df.get_buried_residues("B","D")
print "BD"

# Dimer-Dimer outside-outside
xml2df = pisa_xml_to_dataframe(base_path + pdb + "_no_het_pisa.xml")
dfAD = xml2df.get_buried_residues("A","D")
print "AD"

# Now we will make the lists of shade/tint regions for Texshade.
# 
# Texshade has a frustrating limitation/bug in that shade/tint regions have to be sorted. In addition, we have a couple scenarios where we want to assign a shade or tint to every position that does not meet criteria. To make everything simple, we'll start with a pre-specified, already-sorted dataframe and update it. This is laborious and inelegant but - more important - robust.

residue_list = list(range(0, 400)) 
is_interface_residue = [0] * 400
dfDimerInterface = pd.DataFrame(list(zip(residue_list,is_interface_residue)), columns =['seq_num', 'is_interface_residue'])

for index, row in dfAB.iterrows():
    dfDimerInterface.at[int(row["seq_num"]), 'is_interface_residue'] = 1
    # R33Q has definitive functional/experimental data supporting the conclusion that it affects dimerization, even though it is not buried at an interface. 
    # dfDimerInterface.at[int(33, 'is_interface_residue'] = 1

print dfDimerInterface

output = ""

dimer_tex = ""
for index, row in dfDimerInterface.iterrows():
    if row["is_interface_residue"] == 1:
        dimer_tex = "\\feature{tttop}{1}{" + str(row["seq_num"]) + ".." + str(row["seq_num"]) + "}{---[\colorDimerInterface]}{}\n"
        print dimer_tex 
        output = output + dimer_tex


interface_chain_list = [""] * 400
dfDimerDimerInterface = pd.DataFrame(list(zip(residue_list,is_interface_residue, interface_chain_list)), columns =['seq_num', 'is_interface_residue', 'interface_chain'])

print dfDimerDimerInterface

# The loops below are in order so that a residue that is an interface residue for both A and B chains is called a B chain interface residue.

# outside inside
for index, row in dfAC.iterrows():
    # Do not overwrite.
    dfDimerDimerInterface.at[int(row["seq_num"]), 'is_interface_residue'] = 1
    dfDimerDimerInterface.at[int(row["seq_num"]), 'interface_chain'] = "A"

# outside outside
for index, row in dfAD.iterrows():
    # Do not overwrite.
    dfDimerDimerInterface.at[int(row["seq_num"]), 'is_interface_residue'] = 1
    dfDimerDimerInterface.at[int(row["seq_num"]), 'interface_chain'] = "A"

# inside inside
for index, row in dfBC.iterrows():
    dfDimerDimerInterface.at[int(row["seq_num"]), 'is_interface_residue'] = 1
    dfDimerDimerInterface.at[int(row["seq_num"]), 'interface_chain'] = "B"

# inside outside
# for index, row in dfBD.iterrows():
#     dfDimerDimerInterface.at[int(row["seq_num"]), 'is_interface_residue'] = 1
#     dfDimerDimerInterface.at[int(row["seq_num"]), 'interface_chain'] = "B"

print dfAC
print dfAD

dimer_dimer_tex = ""
for index, row in dfDimerDimerInterface.iterrows():
    if row["is_interface_residue"] == 1 and row["interface_chain"] == "A":
        dimer_dimer_tex = "\\feature{ttttop}{1}{" + str(row["seq_num"]) + ".." + str(row["seq_num"]) + "}{---[\colorInterDimerInterfaceOutside]}{}\n"
        output = output + dimer_dimer_tex

    if row["is_interface_residue"] == 1 and row["interface_chain"] == "B":
        dimer_dimer_tex = "\\feature{ttttop}{1}{" + str(row["seq_num"]) + ".." + str(row["seq_num"]) + "}{---[\colorInterDimerInterfaceInside]}{}\n"
        output = output + dimer_dimer_tex

    print dimer_dimer_tex 

###
import sys 

out_file = "./output/interface_residues_texshade.tex"
with open(out_file, "wb") as f:
    f.write(output)



    # BC_count += 1
    # print "\\feature{top}{1}{" + row["seq_num"] + ".." + row["seq_num"] + "}{---[Blue]}{}"

# AC_count = 0
# for index, row in df.iterrows():
#     AC_count += 1
#     print "\\feature{top}{1}{" + row["seq_num"] + ".." + row["seq_num"] + "}{---[Blue]}{}"

# BD_count = 0
# for index, row in df.iterrows():
#     BD_count += 1
#     print "\\feature{top}{1}{" + row["seq_num"] + ".." + row["seq_num"] + "}{---[Blue]}{}"

# AD_count = 0
# for index, row in df.iterrows():
#     AD_count += 1
#     print "\\feature{top}{1}{" + row["seq_num"] + ".." + row["seq_num"] + "}{---[Blue]}{}"

# AB_count = 0
# for index, row in df.iterrows():
#     AB_count += 1
#     print "\\feature{top}{1}{" + row["seq_num"] + ".." + row["seq_num"] + "}{---[Blue]}{}"

#     # print row["name"]
#     # print row["seq_num"]
#     # print row["bsa"]
