# 读取一个fasta格式的文本文件，
# 输出序列个数，序列总长，最长序列的长度，最短序列的长度，
# 序列中N的个数，序列长度平均值，中位值，GC含量（%）
# 测试用的cpg.fasta是由三条叶绿体基因组组成

from Bio import SeqIO

'''
for seq_record in SeqIO.parse("cpg.fasta","fasta"):
    print("id is ", seq_record.id)
    #print(repr(seq_record.seq))
    print("length is ", len(seq_record))
'''

seq_lengths = [len(seq_record) for seq_record in SeqIO.parse("cpg.fasta","fasta")]
print("1. The number of sequences is ", len(seq_lengths))
print("2. The total length of the sequence is ", sum(seq_lengths))
print("3. The largest sequence length is ", max(seq_lengths))
print("4. The smallest sequence length is ", min(seq_lengths))
print("5. The average sequence length is %.1f" % (sum(seq_lengths) / len(seq_lengths)))

# median
seq_lengths.sort()
half = len(seq_lengths) //2
median = (seq_lengths[half]+seq_lengths[~half]) /2
print("6. The median sequence length is %d" % median)

# 序列转为小写，避免序列名称干扰
for seq_record in SeqIO.parse("cpg.fasta","fasta"):
    seq = seq_record.seq.lower()
    number_G = seq.count('g')
    number_C = seq.count('c')
    number_N = seq.count('n')

percent_GC = (number_C + number_G) / sum(seq_lengths)
print("7. The number of base N is %d" % number_N)
print("8. The percentage of GC is %.2f%%" % (percent_GC*100))
