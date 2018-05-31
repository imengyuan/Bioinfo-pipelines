# 流程和脚本

先align再call SNP
（跑各个步骤还是要把在不同文件夹下，不然结果堆一起都不清楚啥是啥）

<br>

## 01 Align
先按照01.align.md进行比对，需要reads和reference序列

### 流程

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

<br>

### 批量生成脚本
01.align.pl用于生成脚本，批量对每一个fq.gz文件完成align-rmdup-realign的步骤
运行完生成三个sh脚本文件，接下来可以按顺序运行他们（耗时长建议开tmux）
```
sh 01.align.pl.sh;sh 02.rmdup.sh;sh 03.rungatk.sh
```

这个步骤应该还是比较快。这里还可以接着用BamCount和scripts两个文件夹的脚本统计一下输出的结果。

<br>

### 结果分析

1. /BamCount/*.pl
```shell
DepthCoverage.pl #for depth and coverage information  
MapRatio.count.pl #for mapration information  
```

2. /scripts/*.pl
```shell
Base.Depth1.BasicCount.pl #计算每一个深度下对应的碱基数目
Base.Depth2.HistoGram.pl #可以生成全基因组depth柱状统计图：即把depth分成以10为一个区间，合并大于200的所有碱基数；得到每个深度区间中的碱基数目
Base.Depth3.Mean.Depth.pl #用于输出基因组的平均深度 #Base.Depth2与Base.Depth3需要用Base.Depth1的输出结果
GC.contant.pl #统计基因组GC含量分布，将组装的基因组以500bp为窗口，计算每个窗口的GC含量
GC.Depth.pl #统计每个窗口(20k)中GC含量和平均深度
GenomeSize.pl #通过读dict文件，统计基因组大小
```

脚本都能直接用，需要改的地方是文件路径和软件路径。作业是看这些这些步骤输出的结果，上述共8个perl脚本，结果截图都在01align_results.docx。

到这里就完成了所有序列比对的过程，下一步是call SNP。

<br>

## 02 Call SNP 
<!--静下心来认真读readme才是迅速掌握流程的办法-->

### 流程
samtools和gatk都可用于call SNP

* GATK
```
/jre1.8.0_121/bin/java -jar GenomeAnalysisTK.jar -T HaplotypeCaller -R pil.Genome.fa -I bam.list -L scaffold27_cov120 -o scaffold27_cov120.vcf.gz
```

* samtools 
```
samtools mpileup -ug -t DP -t DP4 -f pil.Genome.fa pil500.realn.bam| bcftools call -vmO z -o pil500.vcf.gz
```

<br>

### 生成脚本 

* 02.call.samtools.pl生成02.call.samtools.pl.sh脚本
* 03.call.gatk.chr.pl生成03.call.gatk.chr.pl.sh和03.call.gatk.chr.pl.supp.sh脚本

这两步需要时间稍长，可以在tmux里运行，吃个饭回来刚好（也可能刚去吃饭程序就报错断掉了orz）
```shell
sh 02.call.samtools.pl.sh;03.call.gatk.chr.pl.sh
```

<br>

### 结果分析
有一些计算杂合度的脚本，老师没有给出...
<!--补充vcf格式的笔记-->
call snp之后的结果文件格式为vcf.gz，解压后查看。vcf文件格式前面有很多行注释，表明软件版本等信息，十多行之后是SNP结果。
一些参数含义
```
DP DEPTH
DEP4 AGCT
map quality
GT:PL:DP:SP:DP4 genotype
```

其他脚本

* samtools和gatk产生的结果，可以写一个脚本来统计二者SNP结果的重合。参考overlap.pl或04.overlap.pl
* 另外，可以写一个脚本筛选出（保留前面注释行）SNP值大于30的数据，参考filter.pl

<br>

## Perl笔记
有时间再更
```perl
# %hash
# $hash{$key}=$value

#数组格式 my @name=keys %hash
foreach my $name(@name){
    print"$hash{%name}\n"
}

$hash{"id"}{"gender"}="1"
$hash{"id"}{"name"}="z"
print"#id\tgender\tname\n"
foreach my (keys %hash){
    print"id\t$hash{"id"}{"gender"}\t$hash{"id"}{"name"}\n"
    
}
```














