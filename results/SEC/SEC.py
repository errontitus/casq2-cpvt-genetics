import os
import sys
# import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Buffer: Turbidity Assay Buffer (TAB, 15 mM Tris pH 7.4, 20 mM NaCl, 85 mM KCl) plus 1 mM EDTA
# No calcium

xLabel = "Elution Volume (mL)"
yLabel = "Normalized A280"

def read_chromatogram(filename):
    header = 2
    df = pd.read_csv(filepath_or_buffer=filename, header=header, sep="\t", usecols = ["ml", "mAU"])
    max = df.max()["mAU"].astype(float)
    min = df.min()["mAU"].astype(float)
    df["mAU_norm"] = (df["mAU"].astype(float) - min)/(max - min)
    return df


def plot_vs_WT(df_WT, df_mutant, WT_label, mutant_label, xlabel, ylabel, ylim_max, fig_title, legend_title, legend_position, fig_height, fig_width_multiplier):
    print df_WT

    fig = Figure()
    # A canvas must be manually attached to the figure (pyplot would automatically
    # do it).  This is done by instantiating the canvas with the figure as
    # argument.
    FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3])

#    plt.figure(figsize=(3.5, 2.5))
#    fig = plt.figure()

    x = df_WT["ml"]
    y = df_WT["mAU_norm"]
    WT_line, = ax.plot(x, y, color='black') #, 'b.')
    WT_line.set_label(WT_label)

    x = df_mutant["ml"]
    y = df_mutant["mAU_norm"]
    mutant_line, = ax.plot(x, y, color='red') #, 'r.')
    mutant_line.set_label(mutant_label)

    ax.legend(loc=legend_position, title=legend_title)
    # ax.legend(("WT", mutant_label), loc="upper left", title=legend_title)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0,25)
    ax.set_ylim(0,ylim_max)

    fig.set_size_inches(fig_height * fig_width_multiplier, fig_height)
    fig.tight_layout(pad=0.4)

    return fig


# For debugging
# header = 2
# df = pd.read_csv(filepath_or_buffer=filename, header=header, sep="\t", usecols = ["ml", "mAU"])

matplotlib.rcParams.update({'font.size': 8})
matplotlib.rcParams.update({"legend.handlelength": 0.5})
golden = 1.61803398875

WT_filename = "../../data/SEC/WT 0 mM Ca 1mM EDTA 001.asc"
df_WT = read_chromatogram(WT_filename)

R33Q_filename = "../../data/SEC/R33Q 0 mM Ca 1mM EDTA 001.asc"
df_R33Q = read_chromatogram(R33Q_filename)
                                
Y55C_filename = "../../data/SEC/Y55C 0 mM Ca 1 mM EDTA 001.asc"
df_Y55C = read_chromatogram(Y55C_filename)

S173I_filename = "../../data/SEC/S173I  0 mM Ca 1 mM EDTA 001.asc"
df_S173I = read_chromatogram(S173I_filename)

K180R_filename = "../../data/SEC/K180R 0 mM Ca 1 mM EDTA 001.asc"
df_K180R = read_chromatogram(K180R_filename)

R251H_filename = "../../data/SEC/R251H 0 mM Ca 1 mM EDTA 001.asc"
df_R251H = read_chromatogram(R251H_filename)

P308L_filename = "../../data/SEC/P308L 0 mM Ca 1mM EDTA 001.asc"
df_P308L = read_chromatogram(P308L_filename)

D325E_filename = "../../data/SEC/D325E 0 mM Ca 1 mM EDTA 001.asc"
df_D325E = read_chromatogram(D325E_filename)

########### 
WT_TCEP_filename = "../../data/SEC/WT 0 mM Ca 1 mM EDTA 1 mM TCEP 001.asc"
df_WT_TCEP = read_chromatogram(WT_TCEP_filename)

Y55C_TCEP_filename = "../../data/SEC/Y55C 0 mM Ca 1 mM EDTA 1 mM TCEP 001.asc"
df_Y55C_TCEP = read_chromatogram(Y55C_TCEP_filename)

########### 

WT_low_pH_filename = "../../data/SEC/WT 0 mM Ca 1 mM EDTA MES repeat 001.asc"
df_WT_low_pH = read_chromatogram(WT_low_pH_filename)

R251H_low_pH_filename = "../../data/SEC/R251H 0 mM Ca 1 mM EDTA MES 001.asc"
df_R251H_low_pH = read_chromatogram(R251H_low_pH_filename)

########### 
fig_R33Q = plot_vs_WT(df_WT, df_R33Q, "WT", "R33Q", xLabel, yLabel, 1.1, "", "", "upper left", 2, 1.35)
# Adding an annotation to this particular plot.
ax_list = fig_R33Q.axes
# Should be only one.
ax = ax_list[0]
ax.annotate("Monomer", xy=(20, 0.3), xycoords='data',
    xytext=(17, 0.5), textcoords='data',
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3",color="black"),color="black")
ax.annotate("Dimer", xy=(14, 1.0), xycoords='data',
    xytext=(18, 0.8), textcoords='data',
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3",color="black"),color="black")

fig_R33Q.savefig("./output/SEC_CPVT_mutation_R33Q.pgf")
fig_R33Q.savefig("./output/SEC_CPVT_mutation_R33Q.png")

fig_Y55C = plot_vs_WT(df_WT, df_Y55C, "WT", "Y55C", xLabel, yLabel, 1.1, "", "", "upper left", 2, 1.35)
fig_Y55C.savefig("./output/SEC_CPVT_mutation_Y55C.pgf")
fig_Y55C.savefig("./output/SEC_CPVT_mutation_Y55C.png")

fig_S173I = plot_vs_WT(df_WT, df_S173I, "WT", "S173I", xLabel, yLabel, 1.1, "", "", "upper left", 2, 1.35)
fig_S173I.savefig("./output/SEC_CPVT_mutation_S173I.pgf")
fig_S173I.savefig("./output/SEC_CPVT_mutation_S173I.png")

fig_K180R = plot_vs_WT(df_WT, df_K180R, "WT", "K180R", xLabel, yLabel, 1.1, "", "", "upper left", 2, 1.35)
fig_K180R.savefig("./output/SEC_CPVT_mutation_K180R.pgf")
fig_K180R.savefig("./output/SEC_CPVT_mutation_K180R.png")

fig_R251H = plot_vs_WT(df_WT, df_R251H, "WT", "R251H", xLabel, yLabel, 1.1, "", "", "upper left", 2, 1.35)
fig_R251H.savefig("./output/SEC_CPVT_mutation_R251H.pgf")
fig_R251H.savefig("./output/SEC_CPVT_mutation_R251H.png")

fig_P308L = plot_vs_WT(df_WT, df_P308L, "WT", "P308L", xLabel, yLabel, 1.1, "", "", "upper left", 2, 1.35)
fig_P308L.savefig("./output/SEC_CPVT_mutation_P308L.pgf")
fig_P308L.savefig("./output/SEC_CPVT_mutation_P308L.png")

fig_D325E = plot_vs_WT(df_WT, df_D325E, "WT", "D325E", xLabel, yLabel, 1.1, "", "", "upper left", 2, 1.35)
fig_D325E.savefig("./output/SEC_CPVT_mutation_D325E.pgf")
fig_D325E.savefig("./output/SEC_CPVT_mutation_D325E.png")

########### 

fig_Y55C_TCEP = plot_vs_WT(df_WT_TCEP, df_Y55C_TCEP, "WT w/ TCEP", "Y55C w/ TCEP", xLabel, yLabel, 1.1, "", "", "upper left", 2, 1.35)
fig_Y55C_TCEP.savefig("./output/SEC_CPVT_mutation_Y55C_TCEP.pgf")
fig_Y55C_TCEP.savefig("./output/SEC_CPVT_mutation_Y55C_TCEP.png")

########### 

fig_R251H_low_pH = plot_vs_WT(df_WT_low_pH, df_R251H_low_pH, "WT pH 5.6", "R251H pH 5.6", xLabel, yLabel, 1.1, "", "", "upper left", 2, 1.35)
fig_R251H_low_pH.savefig("./output/SEC_CPVT_mutation_R251H_pH_5.6.pgf")
fig_R251H_low_pH.savefig("./output/SEC_CPVT_mutation_R251H_pH_5.6.png")

# pp = PdfPages('./output/For_Jason_SEC.pdf')
# pp.savefig(pD325E)
# pp.savefig(pP308L)
# pp.savefig(pR33Q)
# pp.savefig(pS173I)
# pp.savefig(pK180R)
# pp.close()