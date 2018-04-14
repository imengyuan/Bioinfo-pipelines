# lectrue 7 transcriptomic assembly Trinity

## transcriptomic assembly
无参考、有参考
Tuxedo Trinity
丰度估计、差异表达分析

Tuxedo suite(tophat cufflinks)

sam
bam(small )
samtools tview bam fasta
IGV view alignments

/home/train128/software/trinityrnaseq-Trinity-v2.6.6

/home/train129/software/trinityrnaseq_r2013-02-25/Trinity.pl --seqType fq --JM 4G --left reads.all.left.fq --right reads.all.right.fq --SS_lib_type RF --CPU 6

/home/train128/software/trinityrnaseq-Trinity-v2.6.6/Trinity --seqType fq --max_memory 50G --left reads.all.left.fq --right reads.all.right.fq --SS_lib_type RF --CPU 6

--seqType fq --max_memory 50G --left reads_1.fq  --right reads_2.fq --CPU 6

ncdu .

/home/train128/software/trinityrnaseq-Trinity-v2.6.6/util/TrinityStats.pl trinity_out_dir/Trinity.fasta



uninstalled
bowtie2 2.3.0
jellyfish 2.2.6


## Trinity protocol
1. collect datax
2. assembly using Trinity

/home/train129/software/trinityrnaseq_r2013-02-25/Trinity.pl --seqType fq --JM 4G --left reads.all.left.fq --right reads.all.right.fq --SS_lib_type RF --CPU 6

TRINITY_HOME/util/TrinityStats.pl trinity_out_dir/Trinity.fasta

3. quality assesment(optional)
4. abundance estimation using RSEM
5. differential expression analysis using edgeR

./Trinity --seqType fq  --left /tmpdata/train128/reads.test.left.fq --right /tmpdata/train128/reads.test.right.fq --SS_lib_type RF --max_memory 4G


