# PSMC, SMC++ & HKA Calculation

## psmc

This software package infers population size history from a diploid sequence using the Pairwise Sequentially Markovian Coalescent (PSMC) model.

Link to Software& README https://github.com/lh3/psmc





### 1. 一般流程

#### 代码

```shell
# 生成fq.gz
#-C50 使用bwa过滤 -d -D过滤深度（平均测序深度的1/2 1/3），得到fq.gz文件一致序列
/data/part2/software/samtools-1.8/samtools mpileup -C50 -uf scaffold37_cov106.fa pil.bam | /data/part2/software/bcftools-1.8/bcftools call -c - | /data/part2/software/vcfutils.pl vcf2fq -d 10 -D 100 | gzip > diploid.fq.gz

#fq.gz转为.psmcfa
/data/part2/software/psmc-0.6.5/utils/fq2psmcfa -q20 diploid.fq.gz > diploid.psmcfa

#.psmcfa转为.psmc 
# -p时间节点
/data/part2/software/psmc-0.6.5/psmc -N25 -t15 -r5 -p "4+25*2+4+6" -o diploid.psmc diploid.psmcfa

# 生成.sh，画图好像不用
/data/part2/software/psmc-0.6.5/utils/psmc2history.pl diploid.psmc | /data/part2/software/psmc-0.6.5/utils/history2ms.pl > ms-cmd.sh

#生成eps格式的图片，mac玉兰油可以直接打开查看，windows要转换一下
#-g numbers of years per generation [15]
# -u absolute mutation rate per nucletidels
/data/part2/software/psmc-0.6.5/utils/psmc_plot.pl diploid diploid.psmc
```

#### 中间结果文件

* .psmcfa
`fq2psmcfa' transforms the consensus sequence into a fasta-like format where the i-th character in the output sequence indicates whether there is at least one heterozygote in the bin [100i, 100i+100)

```shell
# diploid.psmcfa
>scaffold37_cov106
NNTTTTTTTTTTTTTTTTTTTTTTKTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTNNTTTTTTTTTTTTTTTTTNTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTKTTTTTTTTTTTTTTTTTTTTNTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
```

* psmc
psmc infers the population size history. psmc infers the scaled mutation rate, the recombination rate and the free population size parameters.

check the readme for more info about the parameters.

```shell
#diploid.psmc
CC      Brief Description of the file format:
CC        CC  comments
CC        MM  useful-messages
CC        RD  round-of-iterations
CC        LL  \log[P(sequence)]
CC        QD  Q-before-opt Q-after-opt
CC        TR  \theta_0 \rho_0
CC        RS  k t_k \lambda_k \pi_k \sum_{l\not=k}A_{kl} A_{kk}
CC        DC  begin end best-k t_k+\Delta_k max-prob
CC
MM      Version: 0.6.5-r67
MM      pattern:4+25*2+4+6, n:63, n_free_lambdas:28
MM      n_iterations:25, skip:1, max_t:15, theta/rho:5
MM      is_decoding:0
MM      n_seqs:1, sum_L:29597, sum_n:1663
RD      0
LK      0.000000
QD      0.000000 -> 0.000000
RI      inf
TR      0.057828        0.011566
MT      15.000000
MM      C_pi: 1.000000, n_recomb: 340.341409
RS      0       0.000000        1.000000        2.793561        0.008208
```

### 2. 带bootstrap的流程
可能因为用的数据量比较小就没有成功跑出结果？

```shell
utils/fq2psmcfa -q20 diploid.fq.gz > diploid.psmcfa

/data/part2/software/psmc-0.6.5/utils/splitfa diploid.psmcfa > split.psmcfa
/data/part2/software/psmc-0.6.5/psmc -N25 -t15 -r5 -p "4+25*2+4+6" -o diploid.psmc diploid.psmcfa 

seq 100 | xargs -i echo /data/part2/software/psmc-0.6.5/psmc -N25 -t15 -r5 -b -p "4+25*2+4+6" -o round-{}.psmc split.fa >sh
#split.psmcfa

cat diploid.psmc round-*.psmc > combined.psmc

/data/part2/software/psmc-0.6.5/utils/psmc_plot.pl -Y50000 combined combined.psmc
#-Y50000
```

### 3. Assignment: 自行计算物种平均测序深度值，设置-d 和-D参数
<!--没有成功，有问题-->
使用samtools对每个物种的bam文件计算测序其平均测序深度，设置-d 和-D参数，批量对10个物种进行作图。

* 参数设置
```
Here option -d sets and minimum read depth and -D sets the maximum. It is
recommended to set -d to a third of the average depth and -D to twice. 
```

* samtools计算read depth
```
samtools depth /data/part2/00.bam/pil07.realn.bam>07.txt
```

#### 解决

* avg_depth.py 对bam文件计算depth并设置参数
* set_depth.sh 运行第一条命令得到fq.gz
* run.plot.sh 运行后三条命令依次得到psmcfa, psmc, eps文件（可以和set_depth.sh合并）

```shell
#set_depth.sh
for i in /data/part2/00.bam/*bam;do samtools depth $i > ${i##*/}.depth;done
for i in *depth;do python3 avg_depth.py $i;done
for i in *sh;do sh $i;done

#run.plot.sh
for i in *.fq.gz;do fq2psmcfa -q20 $i > ${i%.fq.gz}.psmcfa;done
for i in *.psmcfa;do psmc -N25 -t15 -r5 -p "4+25*2+4+6" -o ${i%.psmcfa}.psmc $i;done
for i in *.psmc;do psmc_plot.pl -g 10 ${i%.psmc} $i;done
```
嗯数据太小最后没有计算出结果，psmcfa文件是空的，psmc都是n，但这个思路是对哒。

<br>

## smcpp

SMC++ is a program for estimating the size history of populations from whole genome sequence data

Link to Software& README: https://github.com/popgenmethods/smcpp

原始数据 scaffold37_cov106.vcf.gz

```shell
#压缩成bgzip格式才能识别
zcat scaffold37_cov106.vcf.gz| /data/part2/software/samtools-1.8/htslib-1.8/bgzip -c>scaffold37_cov106.vcf.bgzip.gz
#建立索引
/data/part2/software/samtools-1.8/htslib-1.8/tabix -p vcf scaffold37_cov106.vcf.bgzip.gz
```

对每个物种群体分别画图
```shell
#peu
smc++ vcf2smc scaffold37_cov106.vcf.bgzip.gz peu.scaffold37_cov106.smc.gz scaffold37_cov106 Pop1:peu01,peu02,peu03,peu04,peu05,peu06,peu07,peu08,peu09,peu10
# estimate可加 --theta 0.00075 --fold
smc++ estimate -o ./ peu.scaffold37_cov106.smc.gz
smc++ plot peu.plot.pdf ./model.final.json
```




## HKA Calculation



<!--所以kha值啥意思，有啥用？-->
原始数据：scaffold37_cov106.vcf.gz
### 计算
* HKA.01.pl 从vcf得到每个个体每个位置变异状态(mis/ref/alt/het)
* HKA.02.pl 从01.pl.out结果文件提取单个物种K值、D值
* HKA.03.pl
* HKA.04.py
* 04.py 同学写的，作用与HKA.04.py相同

### 计算结果文件

* 01.pl.out
```
#scaffold       Pos     PPr     Pang    Pdel    Pfre    Plas    Pnig    Ptr
scaffold37_cov106       59      mis     mis     mis     mis     mis     mis
scaffold37_cov106       93      ref     mis     ref     mis     mis     mis
scaffold37_cov106       95      het     mis     alt     mis     mis     mis

```

* 02.pl屏幕输出
```
PPr:  fixed:32281 poly:54575 
```

* 03.pl.out
```
model.final.json              PPr.scaffold37_cov106.smc.gz
#scaffold       start   end     D       K       GenomeD GenomeK
scaffold        1       1000    82      272     32281   54575
scaffold        10001   2000    122     270     32281   54575
scaffold        20001   3000    84      231     32281   54575
scaffold        30001   4000    40      36      32281   54575
```

