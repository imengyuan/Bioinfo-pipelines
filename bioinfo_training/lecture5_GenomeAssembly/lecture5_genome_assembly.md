# 基因组组装

## Sequening
* whole genome shotgun（全部打断）
* hierarchical shotgun sequencing（分段打断）

denovo genome assembly

* 1st Sanger methods (chain termination)
* 2nd Illumina methods (sequencing by synthesis)
* 3rd Pacbio methods 

## Assembly

assembly paradigms
### greedy
### overlap layput consensus
consensus-> contigs

### DE Brujn graph
* k-mer(substring of length k)
* what makes assembly hard?
* repeat
* coverage depth
* standards to assess th result of assembly
    * contiguity(contig number/length, median/max contig length, N50/NG50/D50)
    * completeness(assembled/estimated genome size, core genes number)
    * correctness(mis-join, repeat compression, unnecessary duplications, Indel/SNPs caused by assembler):align all the reads back to the contigs, look for inconsistencies.

## file format and tools
### file format
* fasta
* fastq


### tools
velvet
[blog](http://www.chenlianfu.com/?p=1635)

按照manual上的for impatient people使用即可，软件编译成功之后，生成两个可执行文件：velveth和velvetg，velveth生成格式化的文件，velvetg在前者基础上生成图、进行组装。然后根据需要设置options参数，上面的博客对参数进行了简单介绍。

velvet manual for impatient people
```
make
./velveth
./velvetg

./velveth sillyDirectory 21 -shortPaired data/test_reads.fa
./velvetg sillyDirectory

./velvetg sillyDirectory -cov_cutoff 5 -read_trkg yes -amos_file yes

./velvetg sillyDirectory -cov_cutoff auto

./velvetg sillyDirectory -exp_cov 19 -ins_length 100

./velvetg sillyDirectory -exp_cov auto

./velveth sillyDirectory 21 -short data/test_reads.fa -long data/test_long.fa
./velvetg sillyDirectory -exp_cov 19

./velvetg sillyDirectory -exp_cov auto
```

velvet参数介绍
```
./velvetg directory [options]

directory：工作路径名

Standard options：

-cov_cutoff <floating-point|auto>：移除低覆盖率的node，默认不移除

-ins_length <integer>：two paired end reads之间的期望距离，默认no read pairing

-read_trkg <yes|no>：在集合中对short read位置进行跟踪，默认不跟踪

-min_contig_lgth <int>：导出到contig.fa文件中的最小contig长度，默认为hash长度的2倍

-amos_file <yes|no>：导出到AMOS文件中，默认不导出（no）

-exp_cov <floating point|auto>：唯一区域的期望覆盖率

Advanced options:

-ins_length2 <int>：两个paired-end reads在第二个short-read数据集中的期望距离，默认否

-ins_length_long <integer>：两个long paired-end reads的期望距离，默认否

-ins_length*_sd <int>：数据集的标准差，默认corresponding length的10%（*代表：nothing，2，_long）

-scaffolding <yes|no>：scaffolding of contigs used paired end information (default: on)
-max_branch_length <integer>：在bubble中的碱基对的最大长度，默认100

-max_divergence <floating-point>：在一个bubble中的两个分支的最大分歧率，默认0.2
-max_gap_count <integer>：在一个bubble中的两个分支比对中允许的最大gap值，默认3

-min_pair_count <integer>：构成两个长contigs的paired end的最小值，默认10

-max_coverage <floating point>：在tour bus后移除高覆盖率的node

-long_mult_cutoff <int>：合并contig的long reads的最小值，默认2

-unused_reads <yes|no>：将不用的reads导出到UnusedReads.fa文件中，默认否

-alignments <yes|no>：导出一个主要的contig并和参照序列对其，默认否
```

repeat
finding repeats: RepeatMasker

gene finding approaches
1. rule-based(start&stop codons)
2. content-based(codon bias, promoter sites)
3. similarity-based(machine learning)
4. ab-initio method(FFT)

# 拟南芥叶绿体基因组注释简介
sequence
feature table-> genbank
gene CDS 






