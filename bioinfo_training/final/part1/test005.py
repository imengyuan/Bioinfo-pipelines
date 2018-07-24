from Bio import SeqIO

f = open("test005.out","w")
seq_lengths = [len(seq_record) for seq_record in SeqIO.parse("genome.fasta","fasta")]


for seq_record in SeqIO.parse("genome.fasta","fasta"):
    seq = seq_record.seq.lower()
    n_A = seq.count('a')
    n_T = seq.count('t')
    n_G = seq.count('g')
    n_C = seq.count('c')

    if len(seq_record) == max(seq_lengths):
        a_longest = seq.count('a')
    if len(seq_record) == min(seq_lengths):
        g_shortest = seq.count('g')

f.write("number of A: "+str(n_A)+"\n")
f.write("number of G: "+str(n_G)+"\n")
f.write("number of C: "+str(n_G)+"\n")
f.write("number of g: "+str(n_G)+"\n")
f.write("a of longest seq:"+str(a_longest)+"\n")
f.write("g of shortest seq:"+str(g_shortest)+"\n")



f.close()
