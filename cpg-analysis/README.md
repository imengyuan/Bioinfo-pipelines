# 叶绿体基因组的组装、注释、修正以及提交

一些说明。

<br>

## 叶绿体基因组的结构及其特点

目前的研究结果表明，高等植物叶绿体基因组的结构非常保守，第一个被测序的高等植物叶绿体基因组为烟草叶绿体基因组，其基因组结构为双链环形DNA分子，有四段式结构，分别是大单拷贝区（large single copy region, LSC），小单拷贝区（small singe copy region, SSC）,反向重复区A(inverted repeat region A, IRA)和反向重复区B(inverted repeat region B, IRB)。两个反向重复区的序列相同，但方向相反，将LSC和SSC分隔开来。被子植物的演化过程中，对于大多数物种来说，其叶绿体基因组这四个部分的结构顺序相同，但不同物种叶绿体基因组之间的差异主要表现为IR区域的扩张和收缩。也有例外，比如豆科植物中的一些植物其叶绿体基因组会完全丢失两个IR区中的一个。

叶绿体基因组作为核外基因组用于植物系统研究具有其自身的优点。
1. 高等植物叶绿体基因组较核基因组小很多，但基因密度较核基因组大。并且其组织结构与基因组成相对保守， 可以在很大种群范围上保证同源性，便于较远进化类群间的系统进化同源比对。
2. 叶绿体作为半自主性复制细胞器，其基因组信息复制和传递遵循母系单性遗传，所有基因为单拷贝，保证了基因在物种间的直系同源性，几乎不存在旁系同源基因干扰。
3. 植物叶绿体基因组中核酸置换速率适中，是核基因组的约五分之一，是植物线粒体基因组的约５倍左右。
4. 叶绿体基因组不同区域进化速率差异显著。受功能保守的限制，其蛋白编码区进化速率较慢，可被广泛应用于较大分类单位的系统进化分析。其非编码序列表现出较快的进化速率，可为系统进化发育分析提供大量的信息，适用于低分类阶元的研究。

![东当归*Angelica acutiloba*的叶绿体结构与注释情况](https://github.com/ViciaYuan/Bioinfo-pipelines/tree/master/cpg-analysis/Angelica_acutiloba.png)
<br>

## 基因组组装的算法原理

参考文献和博客
* [博客-基因组组装算法](https://www.cnblogs.com/leezx/p/5590159.html)
* [Comparison of the two major classes of assembly algorithms: overlap–layout–consensus and de-bruijn-graph](https://academic.oup.com/bfg/article/11/1/25/191455)
* [De novo assembly of human genomes with massively parallel short read sequencing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2813482/)

目前构建Graph的主流方法有3种，Overlap-Layout-Consensus（Celera Assembler、PBcR），de Bruijn Graph（SOAPdenovo） 和 String Graph（Falcon）。本次组装叶绿体基因组用的是SOAPdenovo这个软件，首先将reads打断成长度为K的核酸片段，即Kmer，再利用Kmer间的overlap关系构建de Bruijn 图，再通过de Bruijn图得到基因组序列。

![SOAPdenovo组装算法流程](https://github.com/ViciaYuan/Bioinfo-pipelines/tree/master/cpg-analysis/soapdenovo.png)


<br>

## K值、N50值等的含义

Kmer即长度为k的核苷酸序列，用于构建de Brujin图。使用SOAPdenovo组装基因组时，设置K值的范围，使用范围内每个K值进行组装得到对应的contig文件，将所有的得到的contig文件map到参考序列，并得到最好的k值。根据N50值选出最好的K值。把组装出的contigs或scaffolds从大到小排列，当其累计长度刚刚超过全部组装序列总长度50%时，最后一个contig或scaffold的大小即为N50的大小，N50对评价基因测序的完整性有重要意义。N50最大的K值为最好。这里k值从6到63，组装时使用每个2k+1值，考虑到范围和梯度（？）。


## 线程数的设定

设定为16。根据实验室电脑设置的么。一定要设置用来提高运行速度的么。



<br>

## 新旧脚本的区别
新的脚本在序列两端添加了一段序列，环形区域重合时更为准确。另外新的脚本只有10个步骤，得到的结果还需一代测序补洞。旧的脚本后面不补洞的流程保留，接着运行tablet等程序补洞。旧的脚本写了每一步命令的解释，新的脚本写了每一步运行的输出等，可以先看旧的再看新的。

<br>

## 程序补洞与一代测序补洞的区别
虽然可以用程序补洞，然后再手工修改...但新手很不好把握怎么改，而且改的地方也挺多的也比较费时，结果也不准确。所以这里采用新的脚本获得叶绿体基因组后，设计引物，一代测序补洞，使结果更准确。
<br>










