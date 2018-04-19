
```
yuanmengdeMacBook-Pro:test3 yuanmeng$ sh script.sh
==========================================
======THIS PIPELINE IS MADE BY YUYAN======
======@SICHUAN UNIVERSITY 2017.12.19======
==========================================
Please check the following setting:
clean reads 1: SQ_H3K5YDMXX_L1_1.clean.fq.gz
clean reads 2: SQ_H3K5YDMXX_L1_2.clean.fq.gz
Use K form 13 to 127
Use 16 threads in bowtie2 and samtools
==========================================
START at 2018年 4月18日 星期三 16时27分37秒 CST
Step 1: Download reference sequences in Geneious.
Step 2: Please export the reference sequences to the same folder of this script.
START at 2018年 4月18日 星期三 16时27分39秒 CST
Step 3: Build index for each and combined reference.
START at 2018年 4月18日 星期三 16时29分01秒 CST
Step 4: Map reads to combined reference with bowtie.
23573883 reads; of these:
  23573883 (100.00%) were paired; of these:
    21908791 (92.94%) aligned concordantly 0 times
    34327 (0.15%) aligned concordantly exactly 1 time
    1630765 (6.92%) aligned concordantly >1 times
    ----
    21908791 pairs aligned concordantly 0 times; of these:
      458 (0.00%) aligned discordantly 1 time
    ----
    21908333 pairs aligned 0 times concordantly or discordantly; of these:
      43816666 mates make up the pairs; of these:
        43717567 (99.77%) aligned 0 times
        8290 (0.02%) aligned exactly 1 time
        90809 (0.21%) aligned >1 times
7.28% overall alignment rate
START at 2018年 4月18日 星期三 17时20分07秒 CST
Step 5: Export paird reads from mapped file.
[bam_sort_core] merging from 1 files and 1 in-memory blocks...
START at 2018年 4月18日 星期三 17时24分00秒 CST
Step 6: Map reads to each reference sequence.
START at 2018年 4月18日 星期三 23时41分31秒 CST
Step 7: Find the best reference.
Traceback (most recent call last):
  File "/usr/local/bin/sort", line 7, in <module>
    from sort import cli
  File "/usr/local/lib/python3.6/site-packages/sort.py", line 3
    print('This is suroegin's package - sort')
                            ^
SyntaxError: invalid syntax
The best reference is:
script.sh: line 121: [: DQ898156: unary operator expected
script.sh: line 121: [: GU456628: unary operator expected
script.sh: line 121: [: HM596071: unary operator expected
script.sh: line 121: [: HM596072: unary operator expected
script.sh: line 121: [: HM596073: unary operator expected
script.sh: line 121: [: KM207676: unary operator expected
script.sh: line 121: [: KR002656: unary operator expected
script.sh: line 121: [: KR011054: unary operator expected
script.sh: line 121: [: KR011055: unary operator expected
script.sh: line 121: [: KR048286: unary operator expected
script.sh: line 121: [: KT153021: unary operator expected
script.sh: line 121: [: KT153022: unary operator expected
script.sh: line 121: [: KT781591: unary operator expected
script.sh: line 121: [: KT852844: unary operator expected
script.sh: line 121: [: KT963036: unary operator expected
script.sh: line 121: [: KT963037: unary operator expected
script.sh: line 121: [: KT963038: unary operator expected
script.sh: line 121: [: KT963039: unary operator expected
script.sh: line 121: [: KT983257: unary operator expected
script.sh: line 121: [: KT983258: unary operator expected
script.sh: line 121: [: KU041142: unary operator expected
script.sh: line 121: [: KU041143: unary operator expected
script.sh: line 121: [: KU866529: unary operator expected
script.sh: line 121: [: KU866530: unary operator expected
script.sh: line 121: [: KU866531: unary operator expected
script.sh: line 121: [: KU866532: unary operator expected
script.sh: line 121: [: KU921430: unary operator expected
script.sh: line 121: [: KX118044: unary operator expected
script.sh: line 121: [: KX808491: unary operator expected
script.sh: line 121: [: KX808492: unary operator expected
script.sh: line 121: [: KX808493: unary operator expected
script.sh: line 121: [: KX808494: unary operator expected
script.sh: line 121: [: KY117235: unary operator expected
script.sh: line 121: [: MF594405: unary operator expected
script.sh: line 121: [: MF663725: unary operator expected
script.sh: line 121: [: MG719855: unary operator expected
script.sh: line 121: [: NC_008325: unary operator expected
script.sh: line 121: [: NC_015113: unary operator expected
script.sh: line 121: [: NC_015804: unary operator expected
script.sh: line 121: [: NC_015821: unary operator expected
script.sh: line 121: [: NC_027834: unary operator expected
script.sh: line 121: [: NC_028618: unary operator expected
script.sh: line 121: [: NC_029391: unary operator expected
script.sh: line 121: [: NC_029392: unary operator expected
script.sh: line 121: [: NC_029393: unary operator expected
script.sh: line 121: [: NC_029394: unary operator expected
script.sh: line 121: [: NC_029469: unary operator expected
script.sh: line 121: [: NC_029470: unary operator expected
script.sh: line 121: [: NC_029850: unary operator expected
script.sh: line 121: [: NC_029889: unary operator expected
script.sh: line 121: [: NC_032364: unary operator expected
script.sh: line 121: [: NC_033343: unary operator expected
script.sh: line 121: [: NC_033344: unary operator expected
script.sh: line 121: [: NC_033345: unary operator expected
script.sh: line 121: [: NC_033346: unary operator expected
script.sh: line 121: [: NC_034643: unary operator expected
script.sh: line 121: [: NC_034644: unary operator expected
script.sh: line 121: [: NC_034645: unary operator expected
script.sh: line 121: [: NC_035053: unary operator expected
script.sh: line 121: [: NC_035054: unary operator expected
script.sh: line 121: [: NC_035055: unary operator expected
script.sh: line 121: [: NC_035056: unary operator expected
script.sh: line 121: [: NC_036017: unary operator expected
START at 2018年 4月18日 星期三 23时41分32秒 CST
Step 8: Assemble reads with K from 13 to 127.
^C
yuanmengdeMacBook-Pro:test3 yuanmeng$
```

step7出现了问题，没有正确输出最佳参考序列名称，也没有删除多余的out.sam文件，导致系统硬盘空间不足
跑第8步也需要很长的时间，我暂时终止了程序

```
yuanmengdeMacBook-Pro:test3 yuanmeng$ sh script2.sh
START at 四 4 19 11:07:58 CST 2018
script2.sh: line 3: *2+1: syntax error: operand expected (error token is "*2+1")
yuanmengdeMacBook-Pro:test3 yuanmeng$ sh script2.sh
The best reference is: HM596071
START at 四 4 19 11:10:28 CST 2018
Step 8: Assemble reads with K from 13 to 127.
     1  K51 N50 103 749
     2  K53 N50 107 647
     3  K55 N50 111 616
     4  K57 N50 115 554
     5  K59 N50 119 474
     6  K61 N50 123 392
     7  K63 N50 127 318
     8  K65 N50 131 260
     9  K67 N50 135 51
    10  K69 N50 139 29
    11  K13 N50 253 2
    12  K71 N50 873 12
    13  K73 N50 1238 9
    14  K75 N50 1494 7
    15  K15 N50 2569 8
    16  K77 N50 2857 6
    17  K17 N50 3539 7
    18  K19 N50 3585 8
    19  K21 N50 3813 8
    20  K79 N50 4368 5
    21  K23 N50 5157 7
    22  K27 N50 5191 6
    23  K25 N50 5599 7
    24  K103 N50 6618 7
    25  K49 N50 6638 4
    26  K43 N50 7470 6
    27  K105 N50 7533 6
    28  K107 N50 7822 6
    29  K29 N50 8721 5
    30  K45 N50 9374 4
    31  K39 N50 9450 4
    32  K81 N50 9652 4
    33  K83 N50 9911 5
    34  K31 N50 9942 5
    35  K41 N50 10723 5
    36  K35 N50 11973 4
    37  K109 N50 12265 5
    38  K111 N50 12268 5
    39  K101 N50 12311 6
    40  K99 N50 12510 5
    41  K97 N50 12570 5
    42  K95 N50 12574 5
    43  K93 N50 12600 4
    44  K33 N50 12759 4
    45  K37 N50 13599 3
    46  K85 N50 13763 4
    47  K123 N50 14128 3
    48  K121 N50 14131 3
    49  K119 N50 14149 3
    50  K87 N50 15137 3
    51  K117 N50 15604 3
    52  K115 N50 15622 3
    53  K113 N50 15676 3
    54  K125 N50 15706 3
    55  K89 N50 16361 3
    56  K91 N50 16702 4
    57  K127 N50 24927 2
    58  K47 N50 28063 2
START at 四 4 19 16:47:03 CST 2018
Step 9: Map each contig to reference to find the best K value.
     1  K21 77.10% overall alignment rate
     2  K19 78.10% overall alignment rate
     3  K17 79.26% overall alignment rate
     4  K15 80.84% overall alignment rate
     5  K27 82.28% overall alignment rate
     6  K13 84.36% overall alignment rate
     7  K23 86.31% overall alignment rate
     8  K25 86.66% overall alignment rate
     9  K29 87.67% overall alignment rate
    10  K31 88.17% overall alignment rate
    11  K33 89.43% overall alignment rate
    12  K35 90.14% overall alignment rate
    13  K37 91.03% overall alignment rate
    14  K39 91.15% overall alignment rate
    15  K41 91.86% overall alignment rate
    16  K43 92.01% overall alignment rate
    17  K45 93.06% overall alignment rate
    18  K47 93.43% overall alignment rate
    19  K49 94.00% overall alignment rate
    20  K51 94.12% overall alignment rate
    21  K53 94.63% overall alignment rate
    22  K55 94.65% overall alignment rate
    23  K89 94.78% overall alignment rate
    24  K57 94.85% overall alignment rate
    25  K59 94.98% overall alignment rate
    26  K91 94.99% overall alignment rate
    27  K87 95.05% overall alignment rate
    28  K61 95.37% overall alignment rate
    29  K63 95.38% overall alignment rate
    30  K73 95.46% overall alignment rate
    31  K71 95.49% overall alignment rate
    32  K69 95.54% overall alignment rate
    33  K75 95.54% overall alignment rate
    34  K67 95.61% overall alignment rate
    35  K85 95.62% overall alignment rate
    36  K77 95.64% overall alignment rate
    37  K97 95.71% overall alignment rate
    38  K111 95.72% overall alignment rate
    39  K65 95.75% overall alignment rate
    40  K79 95.88% overall alignment rate
    41  K99 95.92% overall alignment rate
    42  K95 96.00% overall alignment rate
    43  K105 96.01% overall alignment rate
    44  K83 96.01% overall alignment rate
    45  K81 96.11% overall alignment rate
    46  K93 96.31% overall alignment rate
    47  K109 96.50% overall alignment rate
    48  K113 96.59% overall alignment rate
    49  K107 96.83% overall alignment rate
    50  K103 96.89% overall alignment rate
    51  K101 97.09% overall alignment rate
    52  K115 97.16% overall alignment rate
    53  K121 97.83% overall alignment rate
    54  K119 97.91% overall alignment rate
    55  K117 98.01% overall alignment rate
    56  K127 98.10% overall alignment rate
    57  K125 98.41% overall alignment rate
    58  K123 98.58% overall alignment rate
The best K is: K127
START at 四 4 19 16:47:59 CST 2018
Step 10: Combine the contig and map them to the best reference to generate a consensus sequence.
script2.sh: line 66: tools_fasta.pl: command not found
[E::hts_open_format] Failed to open file HM596071.all.out.sam
samtools view: failed to open "HM596071.all.out.sam" for reading: No such file or directory
[mpileup] 1 samples in 1 input files
<mpileup> Set max per-file depth to 8000
Note: the --sample option not given, applying all records
Warning: Sequence "HM596071" not in HM596071.all.vcf.gz
mv: cannot stat 'contig.fas': No such file or directory
mv: cannot stat 'HM596071.all.out.sam': No such file or directory
rm: cannot remove 'HM596071.fasta.*': No such file or directory
rm: cannot remove 'contig.fas': No such file or directory
==========================================
All setps completed.
The best reference is: HM596071
The best K is: K127
The results files could be found in results folder.
End at 四 4 19 16:48:01 CST 2018
==========================================
```

contig map to best ref
Export consensus sequence
Import
clean reads map to consensus
Consensus
combine.contig map tp consesus，根据峰值看洞





