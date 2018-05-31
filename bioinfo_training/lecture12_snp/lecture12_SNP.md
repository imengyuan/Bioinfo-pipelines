# 流程和脚本

先align再call SNP
（跑各个步骤还是要把在不同文件夹下，不然结果堆一起都不清楚啥是啥）

## 01 Align
先按照01.align.md进行比对，需要reads和reference序列

### 一遍流程

1. index genome
```shell
samtools faidx
bwa index
samtools dict x.fa > x.dict
```
2. mapping
```shell
# 不是很懂但先放在这
bwa mem -t 12 -R '@RG\tID:pil01\tSM:pil01\tLB:pil01' scaffold37_cov106.fa pil01.1.fq.gz pil01.2.fq.gz | /data/part2/software/samtools-1.8/samtools sort -O bam -T 02.bwa/pil01 -l 3 -o 02.bwa/pil01.bam -
# -l 3 指压缩等级，可以设置为0(未压缩)~9（压缩效果最好）
# ID SM LB均需要设置为样品编号
# -T为sort bam的prefix 因此 “-T /tmp” 需修改为样品的ID 如 “-T samplexxx”
```
3. remove duplicate
```shell
# 可以用samtool，可以用picard.jar，这里用samtools
samtools rmdup pil01.bam pil01.rmdup.bam
```
4. realign
```shell
# 用的GATK.jar工具（还是等需要用的时候再看怎么改参数吧）
java -Xmx10g -jar GenomeAnalysisTK.jar -R pilGenome.fa -T RealignerTargetCreator -o pil01.intervals -I pil01.rmdup.bam
```

### 批量生成脚本
01.align.pl用于生成脚本，批量对每一个fq.gz文件完成align-rmdup-realign的步骤
运行完生成三个sh脚本文件，接下来可以按顺序运行他们（耗时长建议开tmux）
```
sh 01.align.pl.sh;sh 02.rmdup.sh;sh 03.rungatk.sh
```
上课的用的数据差不多半小时到一小时跑完，每个步骤生成一个对应的文件夹

到这里就完成了所有数据比对的过程，下一步是找出SNP

### 对结果进行分析

1. /BamCount


2. /scripts


## 02 Call SNP 

