from Bio import SeqIO
for seq_record in SeqIO.parse("KT781591.fasta","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
