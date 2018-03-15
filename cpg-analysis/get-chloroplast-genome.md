# 使用总DNA建库获取叶绿体基因组

直接用的老师写的脚本...

## 最终结果的文件结构

```
├── KT781591.fasta
├── KT963036.fasta
├── KT963037.fasta
├── KT963038.fasta
├── KX118044.fasta
├── MF594405.fasta
├── NC_029391.fasta
├── NC_029392.fasta
├── NC_029393.fasta
├── SQ_H3K5YDMXX_L1_1.clean.fq.gz
├── SQ_H3K5YDMXX_L1_2.clean.fq.gz
└── results
    ├── K
    ├── K127.cns.fas
    ├── K127.out.sam
    ├── NC_029391.all.cns.fas
    ├── NC_029391.all.gap.cns.fas
    ├── NC_029391.all.mapped_1.fq
    ├── NC_029391.all.mapped_2.fq
    ├── NC_029391.all.out.sam
    ├── NC_029391.final.cns.fas
    ├── NC_029391.reads.cns.fas
    ├── NC_029391.reads.out.sam
    ├── combine.mapped_1.fq
    ├── combine.mapped_2.fq
    └── logs
```

<br>

## 原始文件的结构为

```
├── script.sh
├── KT781591.fasta
├── KT963036.fasta
├── KT963037.fasta
├── KT963038.fasta
├── KX118044.fasta
├── MF594405.fasta
├── NC_029391.fasta
├── NC_029392.fasta
├── NC_029393.fasta
├── SQ_H3K5YDMXX_L1_1.clean.fq.gz
└── SQ_H3K5YDMXX_L1_2.clean.fq.gz
```

script为使用总DNA建库获取叶绿体基因组流程的脚本；.fasta文件为伞形科其他几种植物的叶绿体基因组参考序列；.clean.fq.gz为测序得到的原始数据。

将整个文件夹拖到终端执行，一晚上差不多就跑完了。

<br>

## 处理流程（script.sh）

跑整个流程时，在每个步骤的代码前添加echo语句作为提示。

<br>

### 0. 初始设定

* 设定clean reads两端文件的文件名
* 设定线程数
* 设定K值的运行范围

<br>

### 1. 在Geneious里下载参考序列

使用下列语句查询
```
#获取当归属叶绿体基因组序列
Angelica[TITLE] AND complete genome[TITLE] AND chloroplast[TITLE]

#或者这个
txid1753[ORGN] AND complete genome[TITLE] AND chloroplast[TITLE]
```

参考序列可以事先拷到和脚本所在文件夹里，1、2步则不用再操作。

<br>

### 2. 将获得的每条序列导出到script.sh所在文件夹，并合并为cp.combine

导出序列

Geneious: File->Export->Batch Export (File Format:FASTA sequences/alignment)

```shell
#合并为cp.combine
cat *.fasta>cp.combine
```

<br>

[bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)是一款将短序列片段定位到参考序列的软件。

[Manual example](http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#getting-started-with-bowtie-2-lambda-phage-example)   [一个介绍算法原理的视频](https://www.bilibili.com/video/av15743137/) 


### 3. 为cp.combine和每一条fasta序列用bowtie2-build建立索引

bowtie2-build [参数] <fasta文件> <前缀>

参数可省，fasta文件可用逗号隔开，前缀用于命名生成索引文件的开头部分。结果重定向到index.log，2>&1表示将标准错误stderr也输出到标准输出stdout当中。

生成的索引文件格式为.1.bt2, .2.bt2, .3.bt2, .4.bt2, .rev.1.bt2和.rev.2.bt2结尾。

```shell
bowtie2-build cp.combine cp.index.combine >index.log 2>&1
for s in $(ls *.fasta); do bowtie2-build $s ${s%.*}.index;done >>index.log 2>&1
```

<br>

### 4. 将clean reads用bowtie2进行比对
<!--这里其他.index文件干啥去了-->

双端测序比对。-x 前缀，-q 输入文件为fastq格式，-1 -2 双末端测序数据，-U 非双末端测序数据，-S 输出的sam格式文件，-p 线程数。

```shell
bowtie2 -x cp.index.combine -q -1 $file1 -2 $file2 -S combine.out.sam -p $threads
```

<br>


### 5. 使用samtools bedtools进行排序和筛选

[Samtools](http://samtools.sourceforge.net/)是一个用来处理和分析SAM和BAM比对文件的集成工具包。[Manual](http://www.htslib.org/doc/samtools.html) ，[一篇博客](http://www.bioinfo-scrounger.com/archives/245)

[Bedtools](http://bedtools.readthedocs.io/en/latest/)BEDTools是可用于genomic features的比较，相关操作及进行注释的工具。这里用bedtools bamtofastq从bam文件提取fastq。

排序。得到排序后的bam文件，以便下一步继续分析。-F 4 过滤掉没有mapping上的reads，-b 输出为bam格式，-@ 线程数，-n 根据read name排序 
```shell
samtools view -F 4 -b -@ $threads combine.out.sam |samtools sort -n > combine.mapped.sort.bam
```

筛选。-fq2需要上面sort加参数-n，生成两个fastq文件
```shell
#得到成对序列的fastq
bedtools bamtofastq -i combine.mapped.sort.bam -fq combine.mapped_1.fq -fq2 combine.mapped_2.fq >no2side.log 2>&1

#获得所有序列的fastq
#bedtools bamtofastq -i combine.mapped.sort.bam -fq combine.mapped.fq
#以下命令获得不成对的mapped序列
#samtools view -F 4 -b -@ $threads out.sam |samtools sort -n -o mapped.sort.sam
#cat mapped.sort.sam |perl -nE 'if(/(^\S+)/){push @{$bp{$1}},$_ }}foreach $key(keys %bp){if(scalar @{$bp{$key}} == 1){print $bp{$key}->[0] }}{'  > mapped_s.fq
##perl这里的匹配没有看懂
```


<br>

### 6. 对每条参考序列依次进行map

shell使用参数扩展字截取符串，${s%.\*.\*.\*} 把name.index.1.bt2里的name提取出来，这个文件来源于第三步每个用参考序列建立的索引文件。

```shell
for s in $(ls *.index.1.bt2); do bowtie2 -x ${s%.*.*} -q -1 combine.mapped_1.fq -2 combine.mapped_2.fq -S ${s%.*.*.*}.out.sam -p $threads > ${s%.*.*.*}.Refstat 2>&1; done
```

<br>

### 7. 挑选最好的参考序列

awk grep、sed是linux操作文本的三大利器，可用于查找、匹配或编辑文本。这里用grep(全面搜索正则表达式并把行打印出来)提取.Refstat文件里的overall alignment rate这个信息。sort -t按空格隔开，-n 按大小排序，-k 2第二列。cat -b给每行编号。这里排在最后的参考序列比对率最高为最好。
```shell
for s in $(ls *.Refstat); do var=$(cat $s| grep "overall alignment rate"); echo "${s%.*} $var";done | sort -t ' ' -nk 2 >best_ref.info
cat -b best_ref.info
```

对best_ref赋值。
```shell
best_ref=$(tail -n 1 best_ref.info|awk -F' ' '{print $1}')
echo "The best reference is: "$best_ref
```

清理sam文件，释放空间
```shell
for s in $(ls *.Refstat);
do
if [ ${s%.*} != $best_ref ]; then  
    rm  ${s%.*}.out.sam
fi
done
```

生成一条consensus序列备用，注意这里samtools sort参数不带-n
<!--有啥用？-->
samtools mpileup搭配bcftools用于call SNP，tabix(a generic indexer for TAB-delimited genome position files)，bcftool consensus生成consensus序列。
```shell
samtools view -F 4 -b -@ $threads $best_ref.out.sam |samtools sort > $best_ref.bam
samtools mpileup -uf $best_ref.fasta $best_ref.bam | bcftools call -mv -Oz -o $best_ref.vcf.gz >>index.log 2>&1
tabix $best_ref.vcf.gz
echo ">$best_ref"_reads >$best_ref.reads.cns.fas
cat $best_ref.fasta | bcftools consensus $best_ref.vcf.gz | sed '1d' >> $best_ref.reads.cns.fas
```
<br>

### 8. SOAPdenovo生成contig，找到N50最大的一个(找到最好的K)

SOAPdenovo是一个可以组装短reads的方法,能构建人类大小基因组的从头组装草图。

```shell
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
```

<br>

### 9. map所有的contig到最好的参考序列

```shell
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

#生成一条consensus序列备用
samtools view -F 4 -b -@ $threads $best_k.out.sam |samtools sort > $best_k.bam
samtools mpileup -uf $best_ref.fasta $best_k.bam | bcftools call -mv -Oz -o $best_k.vcf.gz >>index.log 2>&1
tabix $best_k.vcf.gz
echo ">$best_ref"_best_K >$best_k.cns.fas
cat $best_ref.fasta | bcftools consensus $best_k.vcf.gz | sed '1d' >> $best_k.cns.fas
```

<br>

### 10. 删除特别差的contig，合并剩下的contig，bowtie2到参考序列，生成一条consensus序列备用

```shell
cat *.contig > contig.all
bowtie2 -x $best_ref.index -f contig.all -S $best_ref.all.out.sam -p $threads > $best_ref.all.allstat 2>&1
samtools view -F 4 -b -@ $threads $best_ref.all.out.sam |samtools sort > $best_ref.all.bam
samtools mpileup -uf $best_ref.fasta $best_ref.all.bam | bcftools call -mv -Oz -o $best_ref.all.vcf.gz >>index.log 2>&1
tabix $best_ref.all.vcf.gz
echo ">$best_ref" >$best_ref.all.cns.fas
cat $best_ref.fasta | bcftools consensus $best_ref.all.vcf.gz | sed '1d' >> $best_ref.all.cns.fas

```

补洞流程：将最终生成的all.cns.fas或者可选步骤中生成的.cns.fas，导入Geneious，跟参考序列比对，注释，跟clean reads比对，一代测序补洞。

<br>

以下是不补洞流程。

### 11. 使用Tablet修订

```shell
echo Step 11: Map the combined paired reads to previous consensus sequences.
echo For reads:
bowtie2-build $best_ref.reads.cns.fas $best_ref.reads.index >>index.log 2>&1
bowtie2 -x $best_ref.reads.index -q -1 combine.mapped_1.fq -2 combine.mapped_2.fq -S $best_ref.reads.out.sam -p $threads
echo For $best_ref and $best_k:
bowtie2-build $best_k.cns.fas $best_k.index >>index.log 2>&1
bowtie2 -x $best_k.index -q -1 combine.mapped_1.fq -2 combine.mapped_2.fq -S $best_k.out.sam -p $threads
echo For all contigs:
bowtie2-build $best_ref.all.cns.fas $best_ref.all.index >>index.log 2>&1
bowtie2 -x $best_ref.all.index -q -1 combine.mapped_1.fq -2 combine.mapped_2.fq -S $best_ref.all.out.sam -p $threads

```

<br>

### 12. 分别导入Tablet,看哪个的Feature最少,等待10秒,输入w继续等待,默认为all


```shell
while true;do
    stty -icanon min 0 time 100
    echo "Which is the best consensus sequences? a=all r=reads k=$best_k w=waiting"
    read Arg
    case $Arg in
        a|A)
            Arg="all";
            break;;
        r|R)
            Arg="reads";
            break;;
        k|K)
            Arg=$best_k;
            break;;
        w|W)
            echo "Press any key to continue ...";
            read -n 1;;
        "")  #Autocontinue
            Arg="all";
            break;;
    esac
done
best_seq=$Arg
```

<br>

### 13. 把最好的合并后的序列中没有map上的用N表示（之前所有consensus没map上的都是跟参考序列一致），注意这一步中bcftools call的参数为-m不是-mv


```shell
echo Step 13: Get a clean consensus sequence without gap.
samtools mpileup -uf $best_ref.fasta $best_ref.$best_seq.bam | bcftools call -m -Oz -o $best_ref.$best_seq.gap.vcf.gz >>index.log 2>&1
gunzip $best_ref.$best_seq.gap.vcf.gz
grep "\./\." $best_ref.$best_seq.gap.vcf | awk '{OFS="\t"; if ($0 !~ /\#/); print $1, $2-1, $2}' > $best_ref.$best_seq.gap.bed
bedtools maskfasta -fi $best_ref.$best_seq.cns.fas -bed $best_ref.$best_seq.gap.bed -fo $best_ref.$best_seq.gap.cns.fas
echo ">$best_ref"_all >$best_ref.$best_seq.N.cns.fas
#去除N
var=$(cat $best_ref.$best_seq.gap.cns.fas | sed '1d' | sed 's/N//g')
echo $var | sed 's/ //g' >> $best_ref.$best_seq.N.cns.fas
```

<br>

### 14. 从clean reads中以合并后去N的序列为参考，获得成对fastq


```shell
echo Step 14: Get the paired reads with clean consensus sequence.
bowtie2-build $best_ref.$best_seq.N.cns.fas final.index >>index.log 2>&1
bowtie2 -x final.index -q -1 $file1 -2 $file2 -S $best_ref.$best_seq.out.sam -p $threads
samtools view -F 4 -b -@ $threads $best_ref.$best_seq.out.sam |samtools sort -n > $best_ref.$best_seq.mapped.sort.bam
bedtools bamtofastq -i $best_ref.$best_seq.mapped.sort.bam -fq $best_ref.$best_seq.mapped_1.fq -fq2 $best_ref.$best_seq.mapped_2.fq >no2side.log 2>&1
```

<br>

### 15. 用输出的成对fastq再次对$best_ref.$best_seq.N.cns.fas进行map，作出的consensus即为最终序列$best_ref.final.cns.fas


```shell
echo Step 15: Map the new paired reads to the clean consensus sequence to get the final consensus sequence.
bowtie2 -x final.index -q -1 $best_ref.$best_seq.mapped_1.fq -2 $best_ref.$best_seq.mapped_2.fq -S $best_ref.final.sam -p $threads
samtools view -F 4 -b -@ $threads $best_ref.final.sam |samtools sort > $best_ref.final.bam
samtools mpileup -uf $best_ref.$best_seq.N.cns.fas $best_ref.final.bam | bcftools call -mv -Oz -o $best_ref.final.vcf.gz >>index.log 2>&1
tabix $best_ref.final.vcf.gz
echo ">$best_ref"_final >$best_ref.final.cns.fas
cat $best_ref.$best_seq.N.cns.fas | bcftools consensus $best_ref.final.vcf.gz | sed '1d' >> $best_ref.final.cns.fas
```


<br>

### 16. 移动结果到result文件夹，清理生成的文件，运行完毕输出提示


```

```


<br>

The END.


利用与参考序列比较，从总DNA中得到了进行下一步需要的叶绿体基因组。

下一步是注释、修正、提交。












