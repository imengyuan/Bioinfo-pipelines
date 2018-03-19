# Get chloroplast genome from whole genome

<br>

## Step1-4

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
```


<br>

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

<br>

结果的文件结构
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

## Step5

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

<br>

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

<br>

应该是sam文件有问题，把上一步重新跑了一次，就又没问题了..
```
yuanmengdeMacBook-Pro:test2 yuanmeng$ sh step5.sh
START at 2018年 3月14日 星期三 16时48分34秒 CST
Step 5: Export paird reads from mapped file.
[bam_sort_core] merging from 1 files and 1 in-memory blocks...
FINISH at 2018年 3月14日 星期三 16时52分11秒 CST
now may move onto step 6
```

<br>

日志文件no2side.log tail了一下，貌似全是这种提示，不知道是啥意思
```
*****WARNING: Query ST-E00600:68:H3K5YALXX:2:2488:32606:20196 is marked as paired, but its mate does not occur next to it in your BAM file.  Skipping.
*****WARNING: Query ST-E00600:68:H3K5YALXX:2:2488:32696:13307 is marked as paired, but its mate does not occur next to it in your BAM file.  Skipping.
*****WARNING: Query ST-E00600:68:H3K5YALXX:2:2488:32859:32722 is marked as paired, but its mate does not occur next to it in your BAM file.  Skipping.
```

<br>

## Step67

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

<br>

屏幕输出
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
最后几条参考序列的比对率很接近，差异小可能每次跑的最佳参考序列都不一样。


<br>

## Step8

mac上安装SOAPdenovo最好用brew install Soapdenovo，因为最新版本的SOAPdenovo没有在macOS上编译通过 （[github issue](https://github.com/aquaskyline/SOAPdenovo2/issues/1)），自己下源码编译会报错。另外，下载已经编译好的文件也有问题，并且用brew安装提示没有这个软件...所以找到homebrew GitHub上的[Soapdenovo.rb](https://github.com/Homebrew/homebrew-science/blob/4f15424685012902a94f1a6e2eab0dc6103a2efd/soapdenovo.rb)保存下来，运行brew install Soapdenovo.rb就安装成功了。

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

<br>

估计会跑很久，每一个K值都有以下后缀的文件生成，k从13到127
```
K15.Arc     K15.links   K15.scaf
K15.ContigIndex   K15.markOnEdge    K15.scafSeq
K15.bubbleInScaff K15.newContigIndex  K15.scafStatistics
K15.contig    K15.peGrads   K15.scaf_gap
K15.contigPosInscaff  K15.preArc    K15.updated.edge
K15.edge.gz   K15.preGraphBasic K15.vertex
K15.gapSeq    K15.readInGap.gz
K15.kmerFreq    K15.readOnContig.gz
```

屏幕输出。加起来运行了有约三个半小时

```
Step 8: Assemble reads with K from 115 to 127.
     1  K51 N50 103 686
     2  K53 N50 107 592
     3  K55 N50 111 558
     4  K57 N50 115 504
     5  K59 N50 119 429
     6  K61 N50 123 358
     7  K63 N50 127 278
     8  K65 N50 131 234
     9  K67 N50 161 42
    10  K69 N50 344 24
    11  K71 N50 1167 19
    12  K13 N50 1295 3
    13  K73 N50 1637 15
    14  K77 N50 1637 15
    15  K75 N50 1640 14
    16  K79 N50 2401 13
    17  K81 N50 2516 12
    18  K83 N50 2847 12
    19  K19 N50 2954 10
    20  K17 N50 3524 8
    21  K85 N50 3593 10
    22  K87 N50 3686 11
    23  K101 N50 3703 11
    24  K15 N50 3712 8
    25  K103 N50 3749 12
    26  K105 N50 3867 11
    27  K21 N50 3892 8
    28  K35 N50 4153 7
    29  K43 N50 4171 10
    30  K29 N50 4207 8
    31  K25 N50 4346 7
    32  K91 N50 4416 9
    33  K93 N50 4511 9
    34  K45 N50 4583 8
    35  K95 N50 5030 8
    36  K97 N50 5065 8
    37  K99 N50 5066 8
    38  K107 N50 5069 10
    39  K89 N50 5096 8
    40  K23 N50 5269 7
    41  K37 N50 5502 6
    42  K33 N50 5589 5
    43  K27 N50 5645 7
    44  K41 N50 5658 7
    45  K31 N50 6116 6
    46  K109 N50 6165 8
    47  K39 N50 7051 6
    48  K113 N50 8233 7
    49  K115 N50 8341 7
    50  K47 N50 8786 5
    51  K111 N50 8885 7
    52  K117 N50 9087 6
    53  K49 N50 9248 5
    54  K125 N50 9859 5
    55  K123 N50 9868 6
    56  K119 N50 9875 6
    57  K121 N50 9876 6
    58  K127 N50 12740 4
FINISH at 2018年 3月15日 星期四 19时50分03秒 CST
now may move onto step 9
```
这里可以看到K为127时，N50为12740为最大。

<br>

## Step9

```
#!/bin/sh
#每一个k值对应一个.contig文件
best_ref=$(tail -n 1 best_ref.info|awk -F' ' '{print $1}')
threads=16
echo START at $(date)
#9.依次map所有的contig到最好的参考序列
echo Step 9: Map each contig to reference to find the best K value.
for s in $(ls *.contig); \
do bowtie2 -x $best_ref.index -f $s -S ${s%.*}.out.sam -p $threads > ${s%.*}.Kstat 2>&1; \
done
#查看overall alignment rate
for s in $(ls *.Kstat); \
do var=$(cat $s| grep "overall alignment rate"); echo "${s%.*} $var";done | sort -t ' ' -nk 2 > best_k2.info
cat -b best_k2.info

#根据8和9的结果设定best_k
best_k1_weight=(`cat best_k1.info | sed $'s/ /\t/g'| cat -b|sed $'s/ //g'|sort -t$'\t' -k 2|awk -F'\t' '{print $1}'`)
best_k1_id=(`cat best_k1.info | sed $'s/ /\t/g'| cat -b|sed $'s/ //g'|sort -t$'\t' -k 2|awk -F'\t' '{print $2}'`)
best_k2_weight=(`cat best_k2.info | sed $'s/ /\t/g'| cat -b|sed $'s/ //g'|sort -t$'\t' -k 2|awk -F'\t' '{print $1}'`)
for s in `seq 0 $[${#best_k1_weight[@]}-1]`;
do
echo ${best_k1_id[$s]} $[${best_k1_weight[$s]}] $[${best_k2_weight[$s]}] $[${best_k1_weight[$s]}+${best_k2_weight[$s]}];
done |sort -t$' ' -nk 4 >best_k.info
best_k=$(tail -n 1 best_k.info|awk -F' ' '{print $1}')
echo "The best K is: "$best_k

echo FINISH at $(date)
echo now may move onto step 10
```

屏幕输出。第9步运行地很快。
```
yuanmengdeMacBook-Pro:test2 yuanmeng$ sh step9.sh
START at 2018年 3月15日 星期四 20时02分58秒 CST
Step 9: Map each contig to reference to find the best K value.
     1  K21 76.76% overall alignment rate
     2  K19 77.84% overall alignment rate
     3  K17 79.10% overall alignment rate
     4  K15 80.46% overall alignment rate
     5  K27 81.89% overall alignment rate
     6  K13 83.42% overall alignment rate
     7  K23 86.42% overall alignment rate
     8  K25 86.76% overall alignment rate
     9  K29 87.83% overall alignment rate
    10  K31 88.28% overall alignment rate
    11  K33 89.57% overall alignment rate
    12  K35 90.31% overall alignment rate
    13  K37 91.35% overall alignment rate
    14  K39 91.83% overall alignment rate
    15  K41 92.12% overall alignment rate
    16  K43 92.64% overall alignment rate
    17  K45 94.30% overall alignment rate
    18  K47 94.79% overall alignment rate
    19  K49 94.98% overall alignment rate
    20  K97 95.16% overall alignment rate
    21  K95 95.25% overall alignment rate
    22  K91 95.48% overall alignment rate
    23  K99 95.62% overall alignment rate
    24  K51 95.68% overall alignment rate
    25  K85 95.73% overall alignment rate
    26  K83 95.74% overall alignment rate
    27  K121 95.75% overall alignment rate
    28  K89 95.82% overall alignment rate
    29  K87 95.86% overall alignment rate
    30  K93 95.88% overall alignment rate
    31  K81 96.27% overall alignment rate
    32  K117 96.28% overall alignment rate
    33  K119 96.28% overall alignment rate
    34  K53 96.28% overall alignment rate
    35  K79 96.35% overall alignment rate
    36  K123 96.43% overall alignment rate
    37  K55 96.43% overall alignment rate
    38  K77 96.45% overall alignment rate
    39  K115 96.47% overall alignment rate
    40  K73 96.49% overall alignment rate
    41  K67 96.51% overall alignment rate
    42  K113 96.62% overall alignment rate
    43  K69 96.62% overall alignment rate
    44  K75 96.65% overall alignment rate
    45  K57 96.81% overall alignment rate
    46  K71 96.85% overall alignment rate
    47  K107 96.88% overall alignment rate
    48  K59 96.93% overall alignment rate
    49  K61 96.94% overall alignment rate
    50  K105 96.97% overall alignment rate
    51  K63 96.99% overall alignment rate
    52  K111 97.00% overall alignment rate
    53  K65 97.01% overall alignment rate
    54  K109 97.08% overall alignment rate
    55  K125 97.08% overall alignment rate
    56  K101 97.11% overall alignment rate
    57  K103 97.11% overall alignment rate
    58  K127 99.30% overall alignment rate
The best K is: K127
FINISH at 2018年 3月15日 星期四 20时03分35秒 CST
now may move onto step 10
```
这里看到K127 对应的overall alignment rate也最高。

<br>

## Step10
```
#!/bin/sh
best_ref=$(clear)
threads=16
echo START at $(date)

#10.删除特别差的contig，合并剩下的contig，过滤太短的contig
echo Step 10: Combine the contig and map them to the best reference to generate a consensus sequence.
cat *.contig > contig.all

var=$(cat $best_ref.fasta| sed '1d')
echo ">$best_ref" >${best_ref%.*}.split.fasta
echo ${var:0-10000}$var${var:0:10000}>>${best_ref%.*}.split.fasta

bowtie2-build $best_ref.split.fasta $best_ref.split.index >>index.log 2>&1

```

```
tools_fasta.pl -in contig.all -out contig.fas -cut 150 -function length

bowtie2 -x $best_ref.split.index -f contig.fas -S $best_ref.all.out.sam -p 4 --very-fast --end-to-end > $best_ref.all.allstat 2>&1
samtools view -F 4 -b -@ $threads $best_ref.all.out.sam |samtools sort > $best_ref.all.bam
samtools mpileup -uf $best_ref.split.fasta $best_ref.all.bam | bcftools call -mv -Oz -o $best_ref.all.vcf.gz >>index.log 2>&1
tabix $best_ref.all.vcf.gz
echo ">$best_ref" >$best_ref.all.cns.fas
cat $best_ref.split.fasta | bcftools consensus $best_ref.all.vcf.gz | sed '1d' >> $best_ref.all.cns.fas

echo FINISH at $(date)
echo now may move onto step 11
```

屏幕输出
```
yuanmengdeMBP:test2 yuanmeng$ sh step10.sh
START at 2018年 3月19日 星期一 21时19分58秒 CST
Step 10: Combine the contig and map them to the best reference to generate a consensus sequence.
[mpileup] 1 samples in 1 input files
<mpileup> Set max per-file depth to 8000
Note: the --sample option not given, applying all records
The site KT963036:20996 overlaps with another variant, skipping...
The site KT963036:23251 overlaps with another variant, skipping...
The site KT963036:47842 overlaps with another variant, skipping...
The site KT963036:48166 overlaps with another variant, skipping...
The site KT963036:48210 overlaps with another variant, skipping...
The site KT963036:54989 overlaps with another variant, skipping...
The site KT963036:54993 overlaps with another variant, skipping...
The site KT963036:54998 overlaps with another variant, skipping...
The site KT963036:59805 overlaps with another variant, skipping...
The site KT963036:61121 overlaps with another variant, skipping...
The site KT963036:70760 overlaps with another variant, skipping...
The site KT963036:70761 overlaps with another variant, skipping...
The site KT963036:75507 overlaps with another variant, skipping...
The site KT963036:75509 overlaps with another variant, skipping...
The site KT963036:77997 overlaps with another variant, skipping...
The site KT963036:77998 overlaps with another variant, skipping...
The site KT963036:78007 overlaps with another variant, skipping...
The site KT963036:78422 overlaps with another variant, skipping...
The site KT963036:80260 overlaps with another variant, skipping...
The site KT963036:80261 overlaps with another variant, skipping...
The site KT963036:81430 overlaps with another variant, skipping...
The site KT963036:81971 overlaps with another variant, skipping...
The site KT963036:81972 overlaps with another variant, skipping...
The site KT963036:82471 overlaps with another variant, skipping...
The site KT963036:85572 overlaps with another variant, skipping...
The site KT963036:86155 overlaps with another variant, skipping...
The site KT963036:86156 overlaps with another variant, skipping...
The site KT963036:86612 overlaps with another variant, skipping...
The site KT963036:87578 overlaps with another variant, skipping...
The site KT963036:89084 overlaps with another variant, skipping...
The site KT963036:90664 overlaps with another variant, skipping...
The site KT963036:93738 overlaps with another variant, skipping...
The site KT963036:93739 overlaps with another variant, skipping...
The site KT963036:101282 overlaps with another variant, skipping...
The site KT963036:102058 overlaps with another variant, skipping...
The site KT963036:102060 overlaps with another variant, skipping...
The site KT963036:109674 overlaps with another variant, skipping...
The site KT963036:136845 overlaps with another variant, skipping...
The site KT963036:137496 overlaps with another variant, skipping...
The site KT963036:137554 overlaps with another variant, skipping...
FINISH at 2018年 3月19日 星期一 21时20分41秒 CST
now may move onto step 11
```
最终生成的KT963036.all.cns.fas仅170kb




