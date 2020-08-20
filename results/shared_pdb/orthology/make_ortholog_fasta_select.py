import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

input_fasta = sys.argv[1] 
output_fasta_CASQ2_casq1 = sys.argv[2] 

record_dict = SeqIO.to_dict(SeqIO.parse(input_fasta, "fasta"))

sorted_fasta_select = []
sorted_fasta_select.append(SeqRecord(record_dict["9606.ENSP00000261448"].seq, "CASQ2.Protein.Sequence", '', ''))
sorted_fasta_select.append(SeqRecord(record_dict["9606.ENSP00000357057"].seq, "CASQ1.Protein.Sequence", '', ''))

count = SeqIO.write(sorted_fasta_select, output_fasta_CASQ2_casq1, "fasta")
print("Saved %i records from %s to %s" % (count, input_fasta, output_fasta_CASQ2_casq1))