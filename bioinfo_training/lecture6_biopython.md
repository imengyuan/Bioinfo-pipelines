# biopython模块的使用


## Exercise

* subtest002.py
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