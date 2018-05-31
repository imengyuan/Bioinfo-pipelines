# 群体遗传学基础和重测序分析

## samtools参数
flag 是否比对上
stat 测序深度
merge 合并3个bam
fasidx fasta index
mpileup call snp

zcat peu01.1.part.fq.gz | wc -l #算行数

samtools faidx /tmpdata/train128/snp/part2/00.data/02.reference/scaffold37_cov106.fa
```
[train128@train2018]~/snp% /data/part2/software/samtools-1.8/samtools faidx scaffold37_cov106.fa
[train128@train2018]~/snp% ls
00.align  part2  scaffold37_cov106.fa  scaffold37_cov106.fa.fai
```
/data/part2/software/samtools-1.8/samtools faidx scaffold37_cov106.fa
```
[train128@train2018]~/snp% bwa index scaffold37_cov106.fa
zsh: command not found: bwa
[train128@train2018]~/snp% /data/part2/software/bwa-0.7.17/bwa index scaffold37_cov106.fa
[bwa_index] Pack FASTA... 0.01 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 0.48 seconds elapse.
[bwa_index] Update BWT... 0.01 sec
[bwa_index] Pack forward-only FASTA... 0.00 sec
[bwa_index] Construct SA from BWT and Occ... 0.26 sec
[main] Version: 0.7.17-r1188
[main] CMD: /data/part2/software/bwa-0.7.17/bwa index scaffold37_cov106.fa
[main] Real time: 0.799 sec; CPU: 0.763 sec
[train128@train2018]~/snp% ls
00.align              scaffold37_cov106.fa.amb  scaffold37_cov106.fa.fai
part2                 scaffold37_cov106.fa.ann  scaffold37_cov106.fa.pac
scaffold37_cov106.fa  scaffold37_cov106.fa.bwt  scaffold37_cov106.fa.sa
```

samtools dict scaffold37_cov106.fa > scaffold37_cov106.fa.dict
# 2map
/data/part2/software/bwa-0.7.17/bwa mem -t 12 -R '@RG\tID:pil01\tSM:pil01\tLB:pil01' scaffold37_cov106.fa pil01.1.fq.gz pil01.2.fq.gz | /data/part2/software/samtools-1.8/samtools sort -O bam -T 02.bwa/pil01 -l 3 -o 02.bwa/pil01.bam -

# 3rmdup
samtools rmdup pil01.bam pil01.rmdup.bam

# 4realign
java -Xmx10g -jar GenomeAnalysisTK.jar -R pilGenome.fa -T RealignerTargetCreator -o pil01.intervals -I pil01.rmdup.bam

sh
目录
40行 wc -l
sh 

/data/part2/software/samtools-1.8/samtools dict scaffold37_cov106.fa > scaffold37_cov106.dict


# 读结果
/02.bwa
/data/part2/software/samtools-1.8/samtools view peu01.bam| less -S
scaffold_:0-200000|less

/02.rmdup
bam.bai
tview peu01.bam ../../.fa

# 改脚本统计数据

-S

samtools vcf

DP DEPTH
DEP4 AGCT
map quality
GT:PL:DP:SP:DP4 genotypy 

 perl overlap.pl 02.vcf/scaffold37_cov106.vcf.gz 02.SNPbyChr/scaffold37_cov106/scaffold37_cov106.vcf.gz

%hash
$hash{$key}=$value

数组格式 my @name=keys %hash
foreach my $name(@name){
    print"$hash{%name}\n"
}

$hash{"id"}{"gender"}="1"
$hash{"id"}{"name"}="z"
print"#id\tgender\tname\n"
foreach my (keys %hash){
    print"id\t$hash{"id"}{"gender"}\t$hash{"id"}{"name"}\n"
    
}


zcat 02.vcf/scaffold37_cov106.vcf.gz|grep -c -v  "#"
44241

/data/part2/04.overlap.pl


join("\t",@line),"\n"

x679






