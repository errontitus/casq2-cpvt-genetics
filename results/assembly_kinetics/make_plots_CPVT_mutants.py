import os
import sys
from math import sqrt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib

from lib import BioTek

# Assay conditions:
# Buffer: Turbidity Assay Buffer (TAB, 15 mM Tris pH 7.4, 20 mM NaCl, 85 mM KCl)
# EDTA Dialysis: 10 mM in TAB
# Plate type: uClear, black or clear, half-area
# Calcium: 7 uL of 20 mM Ca added for final concentration of 1 mM
# EDTA: 7 uL of 20 mM EDTA added for final concentration of 1 mM

# Additional mutant D325A requested by reviewer because D325I was a too aggressive substitution.

xLabel = "Minutes after Calcium Addition"
yLabel = "Abs at 350 nm"

# For debugging
# background_offset = BioTek.background_mean_from_matrix(filename, background_matrix_header_row, background_matrix_nrows, "A", "4", "6")
# exit()

# For debugging
# import pandas as pd
# filename = filename
# #cols = ["Kinetic read", "A7", "A8", "A9"]
# header = 21
# nrows = 113
# raw = pd.read_csv(filepath_or_buffer=filename, header=header, sep="\t", nrows=nrows)
# print raw
# exit() 

matplotlib.rcParams.update({'font.size': 8})
matplotlib.rcParams.update({"legend.handlelength": 0.5})
matplotlib.rcParams.update({"legend.frameon": False})
golden = 1.61803398875

def plot_vs_WT_initial_conditions(df_WT, df_Mut, mut_label, title, legend_position="lower right"):
    fig = BioTek.plot_vs_WT(df_WT, df_Mut, mut_label, xLabel, yLabel, 40, 0.2, title, "", legend_position, 1.75, golden)
    file_stem = title.replace(" ", "_")
    fig.savefig("./output/kinetics_" + file_stem + ".pgf")
    fig.savefig("./output/kinetics_" + file_stem + ".pdf")

def plot_vs_WT_MES(df_WT, df_Mut, mut_label, title, legend_position="lower right"):
    fig = BioTek.plot_vs_WT(df_WT, df_Mut, mut_label, xLabel, yLabel, 40, 0.1, title, "", legend_position, 1.75, golden)
    file_stem = title.replace(" ", "_")
    fig.savefig("./output/kinetics_" + file_stem + ".pgf")
    fig.savefig("./output/kinetics_" + file_stem + ".pdf")

def plot_vs_WT_TCEP(df_WT_TCEP, df_Mut_TCEP, df_Mut, WT_label, mut1_label, mut2_label, title, legend_position="lower right"):
#    fig = BioTek.plot_two_vs_WT(df_WT_TCEP, df_Mut_TCEP, df_Mut, mut1_label, mut2_label, xLabel, yLabel, 40, 0.22, title, "", "lower right", 1.75, golden)
    fig = BioTek.plot_two(df_WT_TCEP, df_Mut_TCEP, WT_label, mut1_label, xLabel, yLabel, 40, 0.22, title, "", legend_position, 1.75, golden)
    file_stem = title.replace(" ", "_")
    fig.savefig("./output/kinetics_" + file_stem + ".pgf")
    fig.savefig("./output/kinetics_" + file_stem + ".pdf")

def plot_vs_WT_after_K300(df_WT, df_Mut, mut_label, title):
    fig = BioTek.plot_vs_WT(df_WT, df_Mut, mut_label + " Mg Ca", xLabel, yLabel, 40, 0.2, title, "", "lower right", 1.75, golden)
    file_stem = title.replace(" ", "_")
    fig.savefig("./output/kinetics_" + file_stem + ".pgf")
    fig.savefig("./output/kinetics_" + file_stem + ".pdf")

def plot_mixtures_after_K300(df_WT, df_WT_hemi, df_Mut, df_Mut_Mix, mut_label, title):
    fig = BioTek.plot_mixtures(df_WT, df_WT_hemi, df_Mut, df_Mut_Mix, mut_label, xLabel, yLabel, 40, 0.2, title, "", "lower right", 1.75, golden)
    file_stem = title.replace(" ", "_")
    fig.savefig("./output/kinetics_" + file_stem + ".pgf")
    fig.savefig("./output/kinetics_" + file_stem + ".pdf")

##################### CPVT mutants w/ and w/o Mg, no mixing.
# 1-3: no Mg, 4-6 2 mM Mg
# A	WT	WT	WT	WT	WT	WT
# B	R33Q	R33Q	R33Q	R33Q	R33Q	R33Q
# C	K180R	K180R	K180R	K180R	K180R	K180R
# D	S173I	S173I	S173I	S173I	S173I	S173I
# E	D325E	D325E	D325E	D325E	D325E	D325E
#
# 7-9 no Mg, 10-12 2 mM Mg
# A P308L	P308L	P308L	P308L	P308L	P308L
# B Y55C	Y55C	Y55C	Y55C	Y55C	Y55C
# C R251H	R251H	R251H	R251H	R251H	R251H
# D NP	NP	NP	NP	NP	NP
# E E39K	E39K	E39K	E39K	E39K	E39K

WT_Mg_Ca = BioTek.clean_data_CPVT_Mg_vs_No_Mg(["Kinetic read"], ["A4", "A5", "A6"], "WT")
R33Q_Mg_Ca = BioTek.clean_data_CPVT_Mg_vs_No_Mg(["Kinetic read"], ["B4", "B5", "B6"], "R33Q")
K180R_Mg_Ca = BioTek.clean_data_CPVT_Mg_vs_No_Mg(["Kinetic read"], ["C4", "C5", "C6"], "K180R")
S173I_Mg_Ca = BioTek.clean_data_CPVT_Mg_vs_No_Mg(["Kinetic read"], ["D4", "D5", "D6"], "S173I")
D325E_Mg_Ca = BioTek.clean_data_CPVT_Mg_vs_No_Mg(["Kinetic read"], ["E4", "E5", "E6"], "D325E")
P308L_Mg_Ca = BioTek.clean_data_CPVT_Mg_vs_No_Mg(["Kinetic read"], ["A10", "A11", "A12"], "P308L")
Y55C_Mg_Ca = BioTek.clean_data_CPVT_Mg_vs_No_Mg(["Kinetic read"], ["B10", "B11", "B12"], "Y55C")
R251H_Mg_Ca = BioTek.clean_data_CPVT_Mg_vs_No_Mg(["Kinetic read"], ["C10", "C11", "C12"], "R251H")

plot_vs_WT_initial_conditions(WT_Mg_Ca, R33Q_Mg_Ca, "R33Q", "CASQ2 R33Q Turbidity", "center")
plot_vs_WT_initial_conditions(WT_Mg_Ca, K180R_Mg_Ca, "K180R", "CASQ2 K180R Turbidity", "lower right")
plot_vs_WT_initial_conditions(WT_Mg_Ca, S173I_Mg_Ca, "S173I", "CASQ2 S173I Turbidity", "center")
plot_vs_WT_initial_conditions(WT_Mg_Ca, D325E_Mg_Ca, "D325E", "CASQ2 D325E Turbidity", "lower right")
plot_vs_WT_initial_conditions(WT_Mg_Ca, P308L_Mg_Ca, "P308L", "CASQ2 P308L Turbidity", "center")
plot_vs_WT_initial_conditions(WT_Mg_Ca, Y55C_Mg_Ca, "Y55C", "CASQ2 Y55C Turbidity", "center")
plot_vs_WT_initial_conditions(WT_Mg_Ca, R251H_Mg_Ca, "R251H", "CASQ2 R251H Turbidity", "center")

##################### CPVT mutants in Mg after 300 mM KCl and then back into 85 mM KCl, run with mixing experiments on same plate, same time, all in Mg.

# Row	1	2	3
# A	WT	WT	WT
# B	K180R	K180R	K180R
# C	D325E	D325E	D325E
# D	R33Q	R33Q	R33Q
# E	P308L	P308L	P308L
# F	S173I	S173I	S173I
# G	R251H	R251H	R251H
# H	NP	NP	NP
#		
# Row   4	5	6
# A WT hemi	WT hemi	WT hemi
# B K180R mix	K180R mix	K180R mix
# C D325E mix	D325E mix	D325E mix
# D R33Q mix	R33Q mix	R33Q mix
# E P308L mix	P308L mix	P308L mix
# F S173I mix	S173I mix	S173I mix
# G R251H mix	R251H mix	R251H mix

WT_Mg_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["A1", "A2", "A3"], "WT")
K180R_Mg_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["B1", "B2", "B3"], "K180R")
D325E_Mg_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["C1", "C2", "C3"], "D325E")
R33Q_Mg_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["D1", "D2", "D3"], "R33Q")
P308L_Mg_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["E1", "E2", "E3"], "P308L")
S173I_Mg_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["F1", "F2", "F3"], "S173I")
R251H_Mg_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["G1", "G2", "G3"], "R251H")

# plot_vs_WT_after_K300(WT_Mg_Ca_no_mix, R33Q_Mg_Ca_no_mix, "R33Q", "CASQ2 R33Q in Mg")
# plot_vs_WT_after_K300(WT_Mg_Ca_no_mix, K180R_Mg_Ca_no_mix, "K180R", "CASQ2 K180R in Mg")
# plot_vs_WT_after_K300(WT_Mg_Ca_no_mix, S173I_Mg_Ca_no_mix, "S173I", "CASQ2 S173I in Mg")
# plot_vs_WT_after_K300(WT_Mg_Ca_no_mix, D325E_Mg_Ca_no_mix, "D325E", "CASQ2 D325E in Mg")
# plot_vs_WT_after_K300(WT_Mg_Ca_no_mix, P308L_Mg_Ca_no_mix, "P308L", "CASQ2 P308L in Mg")
# plot_vs_WT_after_K300(WT_Mg_Ca_no_mix, R251H_Mg_Ca_no_mix, "R251H", "CASQ2 R251H in Mg")

WT_Mg_Ca_hemi = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["A4", "A5", "A6"], "WT")
K180R_Mg_Ca_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["B4", "B5", "B6"], "K180R")
D325E_Mg_Ca_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["C4", "C5", "C6"], "D325E")
R33Q_Mg_Ca_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["D4", "D5", "D6"], "R33Q")
P308L_Mg_Ca_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["E4", "E5", "E6"], "P308L")
S173I_Mg_Ca_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["F4", "F5", "F6"], "S173I")
R251H_Mg_Ca_mix = BioTek.clean_data_CPVT_after_K300_Mg(["Kinetic read"], ["G4", "G5", "G6"], "R251H")

# I don't think I want to use these data right now. The high KCl seems to have affected certain mutants differently.
# plot_mixtures_after_K300(WT_Mg_Ca_no_mix, WT_Mg_Ca_hemi, R33Q_Mg_Ca_no_mix, R33Q_Mg_Ca_mix, "R33Q mix", "CASQ2 R33Q mix in Mg")
# plot_mixtures_after_K300(WT_Mg_Ca_no_mix, WT_Mg_Ca_hemi, K180R_Mg_Ca_no_mix, K180R_Mg_Ca_mix, "K180R", "CASQ2 K180R mix in Mg")
# plot_mixtures_after_K300(WT_Mg_Ca_no_mix, WT_Mg_Ca_hemi, S173I_Mg_Ca_no_mix, S173I_Mg_Ca_mix, "S173I", "CASQ2 S173I mix in Mg")
# plot_mixtures_after_K300(WT_Mg_Ca_no_mix, WT_Mg_Ca_hemi, D325E_Mg_Ca_no_mix, D325E_Mg_Ca_mix, "D325E", "CASQ2 D325E mix in Mg")
# plot_mixtures_after_K300(WT_Mg_Ca_no_mix, WT_Mg_Ca_hemi, P308L_Mg_Ca_no_mix, P308L_Mg_Ca_mix, "P308L", "CASQ2 P308L mix in Mg")
# plot_mixtures_after_K300(WT_Mg_Ca_no_mix, WT_Mg_Ca_hemi, R251H_Mg_Ca_no_mix, R251H_Mg_Ca_mix, "R251H", "CASQ2 R251H mix in Mg")


##################### CPVT mutants in Mg after 300 mM KCl and then back into 85 mM KCl, run with mixing experiments on same plate, same time, no Mg.

# Row	1	2	3
# A	WT	WT	WT
# B	K180R	K180R	K180R
# C	D325E	D325E	D325E
# D	R33Q	R33Q	R33Q
# E	P308L	P308L	P308L
# F	S173I	S173I	S173I
# G	R251H	R251H	R251H
# H	NP	NP	NP
#		
# Row   4	5	6
# A WT hemi	WT hemi	WT hemi
# B K180R mix	K180R mix	K180R mix
# C D325E mix	D325E mix	D325E mix
# D R33Q mix	R33Q mix	R33Q mix
# E P308L mix	P308L mix	P308L mix
# F S173I mix	S173I mix	S173I mix
# G R251H mix	R251H mix	R251H mix

WT_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["A1", "A2", "A3"], "WT")
K180R_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["B1", "B2", "B3"], "K180R")
D325E_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["C1", "C2", "C3"], "D325E")
R33Q_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["D1", "D2", "D3"], "R33Q")
P308L_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["E1", "E2", "E3"], "P308L")
S173I_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["F1", "F2", "F3"], "S173I")
R251H_Ca_no_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["G1", "G2", "G3"], "R251H")

WT_Ca_hemi = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["A4", "A5", "A6"], "WT")
K180R_Ca_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["B4", "B5", "B6"], "K180R")
D325E_Ca_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["C4", "C5", "C6"], "D325E")
R33Q_Ca_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["D4", "D5", "D6"], "R33Q")
P308L_Ca_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["E4", "E5", "E6"], "P308L")
S173I_Ca_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["F4", "F5", "F6"], "S173I")
R251H_Ca_mix = BioTek.clean_data_CPVT_after_K300_No_Mg(["Kinetic read"], ["G4", "G5", "G6"], "R251H")

# Not used, same reason as above.
# plot_mixtures_after_K300(WT_Ca_no_mix, WT_Ca_hemi, R33Q_Ca_no_mix, R33Q_Ca_mix, "R33Q mix", "CASQ2 R33Q mix, no Mg")
# plot_mixtures_after_K300(WT_Ca_no_mix, WT_Ca_hemi, K180R_Ca_no_mix, K180R_Ca_mix, "K180R", "CASQ2 K180R mix, no Mg")
# plot_mixtures_after_K300(WT_Ca_no_mix, WT_Ca_hemi, S173I_Ca_no_mix, S173I_Ca_mix, "S173I", "CASQ2 S173I mix, no Mg")
# plot_mixtures_after_K300(WT_Ca_no_mix, WT_Ca_hemi, D325E_Ca_no_mix, D325E_Ca_mix, "D325E", "CASQ2 D325E mix, no Mg")
# plot_mixtures_after_K300(WT_Ca_no_mix, WT_Ca_hemi, P308L_Ca_no_mix, P308L_Ca_mix, "P308L", "CASQ2 P308L mix, no Mg")
# plot_mixtures_after_K300(WT_Ca_no_mix, WT_Ca_hemi, R251H_Ca_no_mix, R251H_Ca_mix, "R251H", "CASQ2 R251H mix, no Mg")


##################### Y55C and R251H special conditions

# 	Column			
# Row	1	2	3			
# A	WT	WT	WT	
# B	R251H	R251H	R251H	
# C	WT	WT	WT	                MES
# D	R251H	R251H	R251H	    MES
# E	WT	WT	WT	                Mg, MES
# F	R251H	R251H	R251H	    Mg, MES
# G	WT	WT	WT	                Mg
# H	R251H	R251H	R251H	    Mg
#
# 	Column			
# Row	4	5	6			
# A   WT_tcep	WT_tcep	WT_tcep
# B   Y55C_tcep	Y55C_tcep	Y55C_tcep
# C   WT_tcep	WT_tcep	WT_tcep             Mg
# D   Y55C_tcep	Y55C_tcep	Y55C_tcep       Mg
# E   Y55C	Y55C	Y55C
# F   Y55C	Y55C	Y55C                    Mg
# G   NP_tcep	NP_tcep	NP_tcep
# H   NP	NP	NP

WT_MES_Only = BioTek.clean_data_CPVT_R251H_and_Y55C(["Kinetic read"], ["C1", "C2", "C3"], "WT")
R251H_MES_Only = BioTek.clean_data_CPVT_R251H_and_Y55C(["Kinetic read"], ["D1", "D2", "D3"], "WT")
WT_Mg_MES = BioTek.clean_data_CPVT_R251H_and_Y55C(["Kinetic read"], ["E1", "E2", "E3"], "WT")
R251H_Mg_MES = BioTek.clean_data_CPVT_R251H_and_Y55C(["Kinetic read"], ["F1", "F2", "F3"], "WT")

WT_TCEP_Mg = BioTek.clean_data_CPVT_R251H_and_Y55C(["Kinetic read"], ["C4", "C5", "C6"], "WT_TCEP")
Y55C_TCEP_Mg = BioTek.clean_data_CPVT_R251H_and_Y55C(["Kinetic read"], ["D4", "D5", "D6"], "Y55C_TCEP_Mg")
Y55C_Mg = BioTek.clean_data_CPVT_R251H_and_Y55C(["Kinetic read"], ["F4", "F5", "F6"], "Y55C_Mg")

plot_vs_WT_MES(WT_MES_Only, R251H_MES_Only, "R251H", "CASQ2 R251H Turbidity pH 5.6 (No Mg)", "upper left")
plot_vs_WT_MES(WT_Mg_MES, R251H_Mg_MES, "R251H", "CASQ2 R251H Turbidity pH 5.6")

plot_vs_WT_TCEP(WT_TCEP_Mg, Y55C_TCEP_Mg, Y55C_Mg, "WT w/ TCEP", "Y55C w/ TCEP", "Y55C", "CASQ2 Y55C Turbidity TCEP", "center")
# plot_vs_WT_initial_conditions(WT_Mg_MES, R251H_Mg_MES, "R251H", "CASQ2 R251H in Mg and MES")


# "Simply mixing would not be expected to capture the complexity of the in vivo env. Need 300 KCl."
# For mutants other than K180R, the defects in filamentation are apparent in the non-Mg condition, as well (supplement)
# Putative ttramer 
# Putative dimer



#df_WT, df_mutant, mutant_label, xlabel, ylabel, xlim_max, ylim_max, fig_title, legend_title, legend_position, fig_height, fig_width_multiplier

# fig_K180R_Mg_Ca = BioTek.plot_vs_WT(WT_Mg_Ca, K180R_Mg_Ca, "K180R Mg Ca", xLabel, yLabel, 40, 0.13, "CASQ2 K180R Mg Ca Turbidity", "", "lower right", 1.75, golden)
# fig_K180R_Mg_Ca.savefig("./output/kinetics_K180R_Mg_Ca.pgf")
# fig_K180R_Mg_Ca.savefig("./output/kinetics_K180R_Mg_Ca.pdf")

# fig_D325E_Mg_Ca = BioTek.plot_vs_WT(WT_Mg_Ca, D325E_Mg_Ca, "D325E Mg Ca", xLabel, yLabel, 40, 0.13, "CASQ2 D325E Mg Ca Turbidity", "", "lower right", 1.75, golden)
# fig_D325E_Mg_Ca.savefig("./output/kinetics_D325E_Mg_Ca.pgf")
# fig_D325E_Mg_Ca.savefig("./output/kinetics_D325E_Mg_Ca.pdf")

# fig_R33Q_Mg_Ca = BioTek.plot_vs_WT(WT_Mg_Ca, R33Q_Mg_Ca, "R33Q Mg Ca", xLabel, yLabel, 40, 0.13, "CASQ2 R33Q Mg Ca Turbidity", "", "lower right", 1.75, golden)
# fig_R33Q_Mg_Ca.savefig("./output/kinetics_R33Q_Mg_Ca.pgf")
# fig_R33Q_Mg_Ca.savefig("./output/kinetics_R33Q_Mg_Ca.pdf")

# fig_P308L_Mg_Ca = BioTek.plot_vs_WT(WT_Mg_Ca, P308L_Mg_Ca, "P308L Mg Ca", xLabel, yLabel, 40, 0.13, "CASQ2 P308L Mg Ca Turbidity", "", "lower right", 1.75, golden)
# fig_P308L_Mg_Ca.savefig("./output/kinetics_P308L_Mg_Ca.pgf")
# fig_P308L_Mg_Ca.savefig("./output/kinetics_P308L_Mg_Ca.pdf")

# fig_S173I_Mg_Ca = BioTek.plot_vs_WT(WT_Mg_Ca, S173I_Mg_Ca, "S173I Mg Ca", xLabel, yLabel, 40, 0.13, "CASQ2 S173I Mg Ca Turbidity", "", "lower right", 1.75, golden)
# fig_S173I_Mg_Ca.savefig("./output/kinetics_S173I_Mg_Ca.pgf")
# fig_S173I_Mg_Ca.savefig("./output/kinetics_S173I_Mg_Ca.pdf")

# fig_R251H_Mg_Ca = BioTek.plot_vs_WT(WT_Mg_Ca, R251H_Mg_Ca, "R251H Mg Ca", xLabel, yLabel, 40, 0.13, "CASQ2 R251H Mg Ca Turbidity", "", "lower right", 1.75, golden)
# fig_R251H_Mg_Ca.savefig("./output/kinetics_R251H_Mg_Ca.pgf")
# fig_R251H_Mg_Ca.savefig("./output/kinetics_R251H_Mg_Ca.pdf")

##########

# fig_K180R_Mg_Ca_mix = BioTek.plot_mixtures(WT_Mg_Ca, WT_Mg_Ca_hemi, K180R_Mg_Ca, K180R_Mg_Ca_mix, "K180R Mg Ca Mix", xLabel, yLabel, 40, 0.13, "CASQ2 K180R Mg Ca Mix Turbidity", "", "lower right", 1.75, golden)
# fig_K180R_Mg_Ca_mix.savefig("./output/kinetics_K180R_Mg_Ca_Mix.pgf")
# fig_K180R_Mg_Ca_mix.savefig("./output/kinetics_K180R_Mg_Ca_Mix.pdf")

# fig_D325E_Mg_Ca_mix = BioTek.plot_mixtures(WT_Mg_Ca, WT_Mg_Ca_hemi, D325E_Mg_Ca, D325E_Mg_Ca_mix, "D325E Mg Ca Mix", xLabel, yLabel, 40, 0.13, "CASQ2 D325E Mg Ca Mix Turbidity", "", "lower right", 1.75, golden)
# fig_D325E_Mg_Ca_mix.savefig("./output/kinetics_D325E_Mg_Ca_Mix.pgf")
# fig_D325E_Mg_Ca_mix.savefig("./output/kinetics_D325E_Mg_Ca_Mix.pdf")

# fig_R33Q_Mg_Ca_mix = BioTek.plot_mixtures(WT_Mg_Ca, WT_Mg_Ca_hemi, R33Q_Mg_Ca, R33Q_Mg_Ca_mix, "R33Q Mg Ca Mix", xLabel, yLabel, 40, 0.13, "CASQ2 R33Q Mg Ca Mix Turbidity", "", "lower right", 1.75, golden)
# fig_R33Q_Mg_Ca_mix.savefig("./output/kinetics_R33Q_Mg_Ca_Mix.pgf")
# fig_R33Q_Mg_Ca_mix.savefig("./output/kinetics_R33Q_Mg_Ca_Mix.pdf")

# fig_P308L_Mg_Ca_mix = BioTek.plot_mixtures(WT_Mg_Ca, WT_Mg_Ca_hemi, P308L_Mg_Ca, P308L_Mg_Ca_mix, "P308L Mg Ca Mix", xLabel, yLabel, 40, 0.13, "CASQ2 P308L Mg Ca Mix Turbidity", "", "lower right", 1.75, golden)
# fig_P308L_Mg_Ca_mix.savefig("./output/kinetics_P308L_Mg_Ca_Mix.pgf")
# fig_P308L_Mg_Ca_mix.savefig("./output/kinetics_P308L_Mg_Ca_Mix.pdf")

# fig_S173I_Mg_Ca_mix = BioTek.plot_mixtures(WT_Mg_Ca, WT_Mg_Ca_hemi, S173I_Mg_Ca, S173I_Mg_Ca_mix, "S173I Mg Ca Mix", xLabel, yLabel, 40, 0.13, "CASQ2 S173I Mg Ca Mix Turbidity", "", "lower right", 1.75, golden)
# fig_S173I_Mg_Ca_mix.savefig("./output/kinetics_S173I_Mg_Ca_Mix.pgf")
# fig_S173I_Mg_Ca_mix.savefig("./output/kinetics_S173I_Mg_Ca_Mix.pdf")

# fig_R251H_Mg_Ca_mix = BioTek.plot_mixtures(WT_Mg_Ca, WT_Mg_Ca_hemi, R251H_Mg_Ca, R251H_Mg_Ca_mix, "R251H Mg Ca Mix", xLabel, yLabel, 40, 0.13, "CASQ2 R251H Mg Ca Mix Turbidity", "", "lower right", 1.75, golden)
# fig_R251H_Mg_Ca_mix.savefig("./output/kinetics_R251H_Mg_Ca_Mix.pgf")
# fig_R251H_Mg_Ca_mix.savefig("./output/kinetics_R251H_Mg_Ca_Mix.pdf")
