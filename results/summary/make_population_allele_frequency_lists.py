import pandas as pd

# Useful columns:
# Entrez Gene Interactor A	Entrez Gene Interactor B	BioGRID ID Interactor A	BioGRID ID Interactor B	Systematic Name Interactor A	Systematic Name Interactor B	Official Symbol Interactor A	Official Symbol Interactor B
filename_2 = "../../data/population_alleles/gnomAD_v2.1.1_ENSG00000118729_2020_02_10_16_03_03.csv"
filename_3 = "../../data/population_alleles/gnomAD_v3_ENSG00000118729_2020_02_10_16_03_55.csv"

header = 0
df = pd.read_csv(filepath_or_buffer=filename_2, header=header, sep=",")
df

for index, row in df.iterrows():
    annotation = row["Annotation"]
    if annotation == "missense_variant":
        count = int(row["Allele Count"])
        if count > 1:
            raw_position = row["Protein Consequence"]
            # print raw_position
            # remove right 3 and left 5 
            position = raw_position[5:-3]
            # print position
            print "\\feature{top}{1}{" + position + ".." + position + "}{---[Red]}{}"

        # This is binary.... enrichment at dimer interface vs tetramer interface.

# Used 
# http://genome.ucsc.edu/cgi-bin/hgTables
# to generate an exon bed file.