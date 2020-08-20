#! /bin/zsh
#

mkdir -p output

python make_ortholog_fasta_select.py "../../../data/orthology/eggnog_calsequestrin_all.fasta" "./output/casq2_casq1.fasta"

clustalo -i ./output/casq2_casq1.fasta -o ./output/casq2_casq1_aligned.fasta --auto --force -v --output-order=input-order --outfmt=clu 