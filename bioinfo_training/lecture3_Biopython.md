# biopython模块的使用

[Tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html)
<br>

## Install
```
pip install biopython
```

## Use
```
# create sequence and complement
my_seq = Seq("AGCTTGCA")
my_seq.complement()
my_seq.reverse_compliment()

# read fasta
from Bio import SeqIO
for seq_record in SeqIO.parse("test.fasta","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

# sequence as strings
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq = Seq("GACTGA",IUPAC.unambiguous_dna)
for index,letter in enumerate(my_seq):
    print("%i %s" % (index,letter))

# seq count
from Bio.Seq import Seq
"AAAA".count("AA") #2
Seq("AAAA").count("AA") #2

# SeqUtils(GC)
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
my_seq = Seq("GACTGA",IUPAC.unambiguous_dna)
GC(my_seq) # 50.0
my_seq[4:10]


# change case
from Bio.Seq import Seq
from Bio.Alphabet import generic_data
dna_seq = Seq("acgAGC",generic_dna)
dna_seq.upper()
dna_seq.lower()

# transcribe, translation



```

## Exercise 

*  subtest002.py
```python
# 读取一个fasta格式的文本文件，
# 输出序列个数，序列总长，最长序列的长度，最短序列的长度，
# 序列中N的个数，序列长度平均值，中位值，GC含量（%）
# 测试用的cpg.fasta是由三条叶绿体基因组组成

from Bio import SeqIO
for seq_record in SeqIO.parse("cpg.fasta","fasta"):
    print("id is ", seq_record.id)
    #print(repr(seq_record.seq))
    print("length is ", len(seq_record))

```

* subtest001.py
```
# 读取两个fasta文件，输出名称同/内容同/名称同但内容不同
# 对于名称同但内容不同的，序列长度是否一致，长度一致的话差异在哪些位置
# 挑出有代表的序列子集

```

* N50_calculate.py
计算velvet组装结果contig.fa的N50值