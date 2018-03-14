# Get chloroplast genome from whole genome

运行脚本step1-4.sh

```shell
#!/bin/sh
#使用总DNA建库获取叶绿体基因组流程
#运行前请清理上次留存的文件
echo ==========================================
echo ======THIS PIPELINE IS MADE BY YUYAN======
echo ======@SICHUAN UNIVERSITY 2017.12.19======
echo ==========================================

###############################################
#############    初始设定    ###################
###############################################
#设定clean reads两端文件的文件名
file1=$1
file2=$2
#设定线程数
threads=16
#设定K的运行范围(6-63之间)，该数值*2+1即为实际的K的范围
K_start=6
K_end=63
###############################################

###############################################
#测试用
#best_ref="NC_033346"
#best_k="K107"
###############################################

###############################################
#如果只有两个fq.gz，则自动获取文件名
if [ "$file1" = "" ] && [ "$file2" = "" ]; then
    filename=(`ls *.fq.gz`)
    if [ ${#filename[@]} = 2 ]; then
        file1=${filename[0]}
        file2=${filename[1]}
    fi
fi
#检查文件是否存在,两端文件是否相同
while true;do
stty -icanon min 0 time 254
if [ -f "$file1" ] && [ -f "$file2" ]; then
    if [ "$file1" = "$file2" ]; then
        echo ERROR: The $file1 is eq to $file2!
        echo Input name of fastq file 1:
        read file1
        echo Input name of fastq file 2:
        read file2
    else
        break
    fi
else
    echo ERROR: Could not found $file1 or $file2!
    echo Input name of fastq file 1:
    read file1
    echo Input name of fastq file 2:
    read file2
fi
done
###############################################
echo Please check the following setting:
echo clean reads 1: $file1
echo clean reads 2: $file2
echo Use K form $[$K_start*2+1] to $[$K_end*2+1]
echo Use $threads threads in bowtie2 and samtools
echo ==========================================
###############################################

#1.使用Angelica[TITLE] AND complete genome[TITLE] AND chloroplast[TITLE]或者txid1753[ORGN] AND complete genome[TITLE] AND chloroplast[TITLE]获取当归属叶绿体基因组序列
echo START at $(date)
echo Step 1: Download reference sequences in Geneious.
 
#2.把所有获得的叶绿体序列每个单独导出到Lab文件夹(Geneious: File->Export->Batch Exports)，并合并成cp.combine
echo Step 2: Please export the reference sequences to the same folder of this script.
for s in $(ls *.fasta); 
do var=$(cat $s| sed '1d');
echo ">${s%.*}.split" >${s%.*}.split;
echo ${var:0-10000}$var${var:0:10000}>>${s%.*}.split; 
done
cat *.split>cp.combine
rm *.split
#3.bowtie2-build 建立索引
echo Step 3: Build index for each and combined reference.
bowtie2-build cp.combine cp.index.combine >index.log 2>&1
for s in $(ls *.fasta); do bowtie2-build $s ${s%.*}.index;done >>index.log 2>&1

#4.将clean reads用bowtie2进行map(-p为线程数)
echo Step 4: Map reads to combined reference with bowtie.
bowtie2 -x cp.index.combine -q -1 $file1 -2 $file2 -S combine.out.sam -p $threads


echo FINISHED at $(date)
echo now move onto step 5
#
```


屏幕输出

```
yuanmengdeMacBook-Pro:test yuanmeng$ sh step1-4.sh
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
START at 2018年 3月14日 星期三 14时44分58秒 CST
Step 1: Download reference sequences in Geneious.
Step 2: Please export the reference sequences to the same folder of this script.
Step 3: Build index for each and combined reference.
Step 4: Map reads to combined reference with bowtie.
23573883 reads; of these:
  23573883 (100.00%) were paired; of these:
    22042095 (93.50%) aligned concordantly 0 times
    8662 (0.04%) aligned concordantly exactly 1 time
    1523126 (6.46%) aligned concordantly >1 times
    ----
    22042095 pairs aligned concordantly 0 times; of these:
      41 (0.00%) aligned discordantly 1 time
    ----
    22042054 pairs aligned 0 times concordantly or discordantly; of these:
      44084108 mates make up the pairs; of these:
        43951042 (99.70%) aligned 0 times
        3330 (0.01%) aligned exactly 1 time
        129736 (0.29%) aligned >1 times
6.78% overall alignment rate
FINISHED at 2018年 3月14日 星期三 15时11分52秒 CST
now move onto step5
yuanmengdeMacBook-Pro:test yuanmeng$

```


结果文件结构
```shell
.
├── KT781591.fasta
├── KT781591.index.1.bt2
├── KT781591.index.2.bt2
├── KT781591.index.3.bt2
├── KT781591.index.4.bt2
├── KT781591.index.rev.1.bt2
├── KT781591.index.rev.2.bt2
├── KT963036.fasta
├── KT963036.index.1.bt2
├── KT963036.index.2.bt2
├── KT963036.index.3.bt2
├── KT963036.index.4.bt2
├── KT963036.index.rev.1.bt2
├── KT963036.index.rev.2.bt2
├── KT963037.fasta
├── KT963037.index.1.bt2
├── KT963037.index.2.bt2
├── KT963037.index.3.bt2
├── KT963037.index.4.bt2
├── KT963037.index.rev.1.bt2
├── KT963037.index.rev.2.bt2
├── KT963038.fasta
├── KT963038.index.1.bt2
├── KT963038.index.2.bt2
├── KT963038.index.3.bt2
├── KT963038.index.4.bt2
├── KT963038.index.rev.1.bt2
├── KT963038.index.rev.2.bt2
├── KX118044.fasta
├── KX118044.index.1.bt2
├── KX118044.index.2.bt2
├── KX118044.index.3.bt2
├── KX118044.index.4.bt2
├── KX118044.index.rev.1.bt2
├── KX118044.index.rev.2.bt2
├── MF594405.fasta
├── MF594405.index.1.bt2
├── MF594405.index.2.bt2
├── MF594405.index.3.bt2
├── MF594405.index.4.bt2
├── MF594405.index.rev.1.bt2
├── MF594405.index.rev.2.bt2
├── NC_029392.fasta
├── NC_029392.index.1.bt2
├── NC_029392.index.2.bt2
├── NC_029392.index.3.bt2
├── NC_029392.index.4.bt2
├── NC_029392.index.rev.1.bt2
├── NC_029392.index.rev.2.bt2
├── NC_029393.fasta
├── NC_029393.index.1.bt2
├── NC_029393.index.2.bt2
├── NC_029393.index.3.bt2
├── NC_029393.index.4.bt2
├── NC_029393.index.rev.1.bt2
├── NC_029393.index.rev.2.bt2
├── SQ_H3K5YDMXX_L1_1.clean.fq.gz
├── SQ_H3K5YDMXX_L1_2.clean.fq.gz
├── combine.out.sam
├── cp.combine
├── cp.index.combine.1.bt2
├── cp.index.combine.2.bt2
├── cp.index.combine.3.bt2
├── cp.index.combine.4.bt2
├── cp.index.combine.rev.1.bt2
├── cp.index.combine.rev.2.bt2
├── index.log
└── step1-4.sh
```


运行时间约为27分钟，其中生成的combine.out.sam文件有17.71GB，第4步运行的时间最长。

<br>

## step5

```
#5.使用samtools和bedtools进行排序和筛选(-@为线程数)
echo START at $(date)
echo Step 5: Export paird reads from mapped file.
samtools view -F 4 -b -@ $threads combine.out.sam |samtools sort -n > combine.mapped.sort.bam
#获得成对序列的fastq
bedtools bamtofastq -i combine.mapped.sort.bam -fq combine.mapped_1.fq -fq2 combine.mapped_2.fq >no2side.log 2>&1
#获得所有序列的fastq
#bedtools bamtofastq -i combine.mapped.sort.bam -fq combine.mapped.fq
#以下命令获得不成对的mapped序列
#samtools view -F 4 -b -@ $threads out.sam |samtools sort -n -o mapped.sort.sam
#cat mapped.sort.sam |perl -nE 'if(/(^\S+)/){push @{$bp{$1}},$_ }}foreach $key(keys %bp){if(scalar @{$bp{$key}} == 1){print $bp{$key}->[0] }}{'  > mapped_s.fq
echo FINISH at $(date)
echo now may move onto step 6
```
出现了问题
```
yuanmengdeMacBook-Pro:test yuanmeng$ sh step5.sh
START at 2018年 3月14日 星期三 15时30分38秒 CST
Step 5: Export paird reads from mapped file.
[W::sam_read1] Parse error at line 2
samtools sort: truncated file. Aborting
FINISH at 2018年 3月14日 星期三 15时30分38秒 CST
now may move onto step 6
```
把上一步重新跑了一次，就又没问题了..

```
yuanmengdeMacBook-Pro:test2 yuanmeng$ sh step5.sh
START at 2018年 3月14日 星期三 16时48分34秒 CST
Step 5: Export paird reads from mapped file.
[bam_sort_core] merging from 1 files and 1 in-memory blocks...
FINISH at 2018年 3月14日 星期三 16时52分11秒 CST
now may move onto step 6
```

日志文件no2side.log tail了一下，貌似全是这种提示，不知道是啥意思

```
*****WARNING: Query ST-E00600:68:H3K5YALXX:2:2488:32606:20196 is marked as paired, but its mate does not occur next to it in your BAM file.  Skipping.
*****WARNING: Query ST-E00600:68:H3K5YALXX:2:2488:32696:13307 is marked as paired, but its mate does not occur next to it in your BAM file.  Skipping.
*****WARNING: Query ST-E00600:68:H3K5YALXX:2:2488:32859:32722 is marked as paired, but its mate does not occur next to it in your BAM file.  Skipping.
```

## step67

```shell
#6.对所有参考序列依次进行map
threads=16
echo START at $(date)
echo Step 6: Map reads to each reference sequence.
for s in $(ls *.index.1.bt2); do bowtie2 -x ${s%.*.*} -q -1 combine.mapped_1.fq -2 combine.mapped_2.fq -S ${s%.*.*.*}.out.sam -p $threads > ${s%.*.*.*}.Refstat 2>&1; done

#7.显示统计数字，挑选最好的参考序列(排列最后一个为最好)
echo Step 7: Find the best reference.
for s in $(ls *.Refstat); do var=$(cat $s| grep "overall alignment rate"); echo "${s%.*} $var";done | sort -t ' ' -nk 2 >best_ref.info
cat -b best_ref.info
#lab中最好的是NC_029392(NC_029392    99.35% overall alignment rate)，对best_ref赋值。
best_ref=$(tail -n 1 best_ref.info|awk -F' ' '{print $1}')
echo "The best reference is: "$best_ref

echo FINISH at $(date)
echo now may move onto step 8
```

```
yuanmengdeMacBook-Pro:test2 yuanmeng$ sh step67.sh
START at 2018年 3月14日 星期三 18时48分25秒 CST
Step 6: Map reads to each reference sequence.
Step 7: Find the best reference.
     1  KX118044 36.52% overall alignment rate
     2  MF594405 97.79% overall alignment rate
     3  KT963037 97.94% overall alignment rate
     4  NC_029392 97.94% overall alignment rate
     5  KT781591 98.47% overall alignment rate
     6  KT963038 98.56% overall alignment rate
     7  NC_029393 98.56% overall alignment rate
     8  KT963036 98.65% overall alignment rate
The best reference is: KT963036
FINISH at 2018年 3月14日 星期三 19时15分03秒 CST
now may move onto step 8
```
后面几个的比对率很接近，会不会每次跑best reference都不一样啊

我的天呐soapdenovo太难装了

```
#!/bin/sh
best_ref=$(tail -n 1 best_ref.info|awk -F' ' '{print $1}')
#清理sam文件，释放空间
for s in $(ls *.Refstat);
do
if [ ${s%.*} != $best_ref ]; then  
    rm  ${s%.*}.out.sam
fi
done
#8.SOAPdenovo生成contig，找到N50最大的一个(找到最好的K)
threads=16
K_start=6
K_end=63
echo START at $(date)
echo Step 8: Assemble reads with K from $[$K_start*2+1] to $[$K_end*2+1].
#建立config.txt
echo "max_rd_len=500" > config.txt
echo "[LIB]" >> config.txt
echo "avg_ins=350" >> config.txt
echo "reverse_seq=0" >> config.txt
echo "asm_flags=3" >> config.txt
echo "rank=1" >> config.txt
echo "pair_num_cutoff=3" >> config.txt
echo "map_len=32" >> config.txt 
echo "q1=combine.mapped_1.fq" >> config.txt
echo "q2=combine.mapped_2.fq" >> config.txt
#运行拼接
for s in `seq $K_start $K_end`; do SOAPdenovo-127mer all -s config.txt -o K$[$s*2+1] -p $threads -K $[$s*2+1] -d 5 -R; rm K$[$s*2+1].path; done >SOAPdenovo.log  2>&1
#查看N50
for s in $(ls *.scafStatistics); do var=$(head -n 50 $s| grep "\<N50\>"| sed $'s/\t/ /g'); echo "${s%.*} $var"; done| sort -t$' ' -nk 3 > best_k1.info
cat -b best_k1.info

echo FINISH at $(date)
echo now may move onto step 9
```
