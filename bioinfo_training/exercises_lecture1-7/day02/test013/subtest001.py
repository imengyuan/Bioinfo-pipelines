# 读取两个fasta文件，输出名称同/内容同/名称同但内容不同
# 对于名称同但内容不同的，序列长度是否一致，长度一致的话差异在哪些位置
# 挑出有代表的序列子集

from Bio import SeqIO
'''
for seq_record in SeqIO.parse("KT963036.fasta","fasta"):
    print("id is ", seq_record.id)
    #print(repr(seq_record.seq))
    print("length is ", len(seq_record))
'''
'''
seq_id1 = [seq_record.id for seq_record in SeqIO.parse("cp1.fasta","fasta")]
seq_id2 = [seq_record.id for seq_record in SeqIO.parse("cp2.fasta","fasta")]
'''
record_1 = list(SeqIO.parse("cp1.fasta","fasta"))
record_2 = list(SeqIO.parse("cp2.fasta","fasta"))

same_name = []
same_content = []
diff_content = []
same_length = []
location = []

for record1 in record_1:
    for record2 in record_2:
        if record1.id == record2.id:
            same_name.append(record1.id)
        if record1.seq == record2.seq:
            same_content.append(record1.id)
        if record1.id == record2.id and record1.seq != record2.seq:
            diff_content.append(record1.id)
            if len(record1) == len(record2):
                same_length.append("same length")
                location.append([record1,record2])
            else:
                same_length.append("different length")


for id in location:
    print(record_1[id[]])



print("sequences with same name are ", same_name)
print("sequences with same content are ", same_content)
print("sequences with same name& different content are ", diff_content)
print("and their seq_length are ", dict(zip(diff_content,same_length)))
#print()