# 无参转录组分析Pipeline

[基因课](http://www.genek.tv/my/course/63)视频教程的笔记，整理以作自己以后参考。

注：一些数据链接可能已更改，一些命令也不完整，只是记重要流程。

<!--记得加上以前onenote上的笔记
博客详细内容整理为笔记
闲了再更新吧-->
<br>

## 准备工作

安装bioconda
```
#install 
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh 
Sh .sh 
source ~/.bashrc 加入环境变量 

#Use 
conda install 
conda config --add channels bioconda 
conda config --add channels r 
conda search  
conda install bwa=0.7.12卸载原版本再安装        
conda list 
conda update 
conda remove 

#add channel
conda config —add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/ 
conda config —add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ 
conda config —add channels https://nanomirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/ 

conda config --set show_channel_urls yes 
```
bioconda安装Trinity
```
conda install trinity
```

手动安装Trinity
```
#下载
wget https://github.com/trinityrnaseq/trinityrnaseq/releases
#安装
cd software
tar -zxvf Trinity-v2.4.0.tar.gz
cd trinityrnaseq-Trinity-v2.4.0
make
make plugins
```

数据链接到自己存原始数据的目录并解压
```
/raw_data
ln -s ~/GenekTVExampleData/Transcriptome/rna_reads.small.tar.gz
tar
```

<br>

## 数据预处理 

### quality control: fastqc

```
/QC_before_filter
fastqc options
-o #output dir
--nogroup 
```

原始数据的质控和批量生成脚本[原文链接](http://www.genek.tv/article/25)

单个测试
```
fastqc -o ./ --nogroup ../raw_data/.fastq.gz
```

批量任务
```
ls ../raw_data/*.fastq.gz | xargs -i echo nohup fastqc -o ./ --nogroup{} \& >fastqc.sh
```


### filter: trimmomatic
sample.txt 组名 重复名 read1 
read2

/Filter

/clean_data

filter.sh
```
trimmomatic PE ../raw_data/hcc1395_normal_rep1_r1.fastq.gz ../raw_data/hcc1395_normal_rep1_r1.fastq.gz ../clean_data/normal_rep1_forward_paired.fq.gz ../clean_data/normal_rep1_forward_unpaired.fq.gz ../clean_data/normal_rep1_reverse_paired.fq.gz ../clean_data/normal_rep1_reverse_unpaired.fq.gz ILLUMINACLIP:/home/u179970/miniconda3/share/trimmomatic-0.36-4/adapters/TruSeq3-PE-2.fa:2:30:10 LEADING:5 TRAILING:5 SLIDINGWINDOW:4:5 MINLEN:25 

:%s/normal_rep1/{}/g

awk'{print $2}' ../sample.txt | args -i echo abovecode \& |less -S

awk'{print $2}' ../sample.txt | args -i echo abovecode \& >filter.sh

nohup sh filter.sh &
#每个生成四个文件 保留forward_paired.fq.gz
```

<br>

## 转录本拼接

### assembly: Trinity
```
/Assembly
#把软件路径添加到环境变量
vi ~/.bashrc -> add a new line -> source ./bashrc

export PATH="/home/ubuntu/miniconda3/bin/:$PATH"
trinity-2.6.6
Trinity options:
--seqtype
--max_memory
--samples_file

cp ../sample.txt ./
raw_data/hcc1234_normal_rep1_r1.fastq.gz ->
clean_data/normal_rep1_forward_paired.fq.gz 

:%s/raw_data/\.\./clean_data/g
% all text g all this line

:%s/hcc1396_//g

run_Trinity.sh
nohup /home/zxd/software/trinityrnaseq-Trinity-v2.4.0/Trinity --seqType fq --max_memory 4G --CPU 1 --samples_file ../sample.txt --SS_lib_type RF >trinity.log 2>trinity.err &

sh run_Trinity.sh
tail Trinity.log

result Trinity.fasta
```

### access the results: BUSCO
```
/Assembly_Stat
vi Assembly_Stat.sh
home/u179970/miniconda3/opt/trinity-2.4.0/util/TrinityStats.pl ../Assembly/trity_out_dir/Trinity.fasta > Assembly_Stat.txt

mkdir -p database/busco
wget http://busco.ezlab.org/v2/datasets/endopterygota_odb9.tar.gz tar

busco/
run_BUSCO.sh
perl /home/u179970/miniconda3/opt/trinity-2.4.0/util/misc/get_longest_isoform_seq_per_trinity_gene.pl* ../Assembly/trity_out_dir/Trinity.fasta >longest_isoform.fasta

busco -i longest_isoform.fasta #Trinity.fasta
-l /home/u179970/db/busco/_odb9
-o buscoresult
-m trans
--cpu 2

nohup sh run_busco.sh #run for hours,here 5300/60=90min
#results Complete larger than 80% BUSCO access http://www.genek.tv/course/63/task/715/show
```

<br>

## 表达定量Quantification

方法 基于比对bowtie2 RSEM/eXpress,不基于Kallisto Salmon
```shell
/Quantification
#run_quantification.sh

TRINITY_HOME=/home/genektv/miniconda2/opt/trinity-2.4.0
transcripts=../Assembly/trinity_out_dir/Trinity.fasta
samples_file=../Assembly/sample.txt

$TRINITY_HOME/util/align_and_estimate_abundance.pl \
    --transcripts $transcripts \
    --samples_file $samples_file \
    --seqType fq \
    --SS_lib_type RF \
    --est_method RSEM \
    --aln_method bowtie2 \
    --thread_count 26 \
    --prep_reference \
    --trinity_mode
#rsem每个样品生成一个文件夹。包含bowtie2.bam,bowtie2.bam.ok,RSEM.genes.results,RSEM.isoforms.results,RSEM.isoforms.results.ok,RSEM.stat
#整合成矩阵文件
ls */RSEM.genes.results >genes.quant_files.txt

$TRINITY_HOME/util/abundance_estimates_to_matrix.pl \
    --est_method RSEM \
    --cross_sample_norm TMM \
    --name_sample_by_basedir \
    --quant_files genes.quant_files.txt \
    --out_prefix genes
#output:genes.counts.matrix,genes.guant_files.txt,gene.TPM.not_cross_nom etc
samtools view .bam | less -S

/Assembly_Stat #can wait
vi Assembly_Stat.sh #improve a little
TRINITY_HOME=/home/genektv/miniconda2/opt/trinity-2.4.0
transcripts=../Assembly/trinity_out_dir/Trinity.fasta
isoforms_TMM_EXPR_matrix=../Quantification/isoforms.TMM.EXPR.matrix
#N50
$TRINITY_HOME/util/TrinityStats.pl  $transcripts > Assembly_Stat.txt
#ExN50
$TRINITY_HOME/util/misc/contig_ExN50_statistic.pl $isoforms_TMM_EXPR_matrix $transcripts >ExN50_Stat.txt
#filter
#$TRINITY_HOME/util/filter_low_expr_transcripts.pl --matrix $isoforms_TMM_EXPR_matrix --transcripts $transcripts --min_expr_any 0.1 --trinity_mode >filtered.fasta
```

<br>

## 功能注释 Annotation

```conda install transdecoder
conda install sqlite
conda install blast
conda install hmmer
#optional: signalP、tmhmm、RNAMMER
/software
wget https://github.com/Trinotate/Trinotate/archive/v3.0.2.tar.gz
tar -zxvf v3.0.2.tar.gz

/db/Trinotate 
vi Build_Trinotate_db.sh
TRINOTATE_HOME=/home/genektv/software/Trinotate-3.0.2
$TRINOTATE_HOME/admin/Build_Trinotate_Boilerplate_SQLite_db.pl  Trinotate20171021
gunzip uniprot_sprot.dat.gz

makeblastdb -in uniprot_sprot.pep -dbtype prot
diamond makedb --db uniprot_sprot.pep --in uniprot_sprot.pep#dmnd

gunzip Pfam-A.hmm.gz
hmmpress Pfam-A.hmm

nohup sh Build_Trinotate_db.sh &
#wait for sometime try for some times,check the files
```

```
/Annotation
/step1_run_transdecoder
conda install diamond
vi run_transdecoder.sh
#!/bin/bash
transcripts=../../Assembly/trinity_out_dir/Trinity.fasta
uniprot_sprot_db=/home/genektv/database/Trinotate/uniprot_sprot.pep
Pfam=/home/genektv/database/Trinotate/Pfam-A.hmm

#1.初步筛选ORF
TransDecoder.LongOrfs -S -t $transcripts

#2.与已知蛋白数据库比对（可选）
diamond blastp --query Trinity.fasta.transdecoder_dir/longest_orfs.pep \
        --db $uniprot_sprot_db  \
        --max-target-seqs 1 \
        --outfmt 6 \
        --evalue 1e-5 \
        --threads 10 \
        > Trinity.fasta.transdecoder_dir/longest_orfs.pep.blastp.outfmt6

hmmscan --cpu 8 \
        --domtblout Trinity.fasta.transdecoder_dir/longest_orfs.pep.pfam.domtblout \
        $Pfam \
        Trinity.fasta.transdecoder_dir/longest_orfs.pep

#3.进一步筛选ORF
TransDecoder.Predict -t $transcripts \
        --retain_pfam_hits Trinity.fasta.transdecoder_dir/longest_orfs.pep.pfam.domtblout \
        --retain_blastp_hits Trinity.fasta.transdecoder_dir/longest_orfs.pep.blastp.outfmt6

nohup sh run_transdecoder.sh
```

```
/step2_run_blast_hmmer
vi run_blast_hmmer.sh

transcripts=../../Assembly/trinity_out_dir/Trinity.fasta
proteins=../step1_run_transdecoder/Trinity.fasta.transdecoder.pep
uniprot_sprot_db=/home/genektv/database/Trinotate/uniprot_sprot.pep
Pfam=/home/genektv/database/Trinotate/Pfam-A.hmm

#blastx -query $transcripts -db $uniprot_sprot_db -num_threads 8 -max_target_seqs 1 -outfmt 6 > blastx.outfmt6
diamond blastx --query $transcripts --db $uniprot_sprot_db --threads 8 --max-target-seqs 1 --outfmt 6 > blastx.outfmt6

#blastp -query $proteins -db $uniprot_sprot_db -num_threads 8 -max_target_seqs 1 -outfmt 6 > blastp.outfmt6
diamond blastp --query $proteins --db $uniprot_sprot_db --threads 8 --max-target-seqs 1 --outfmt 6 > blastp.outfmt6

hmmscan --cpu 8 --domtblout TrinotatePFAM.out $Pfam $proteins > pfam.log

nohup sh run_blast_hmmer.sh
```

```
#step3
~/db/Trinotate
sqlite3 .sqlite
.table
.head on
select * from limit 5;
.quit
/step3_run_trinotate
vi run_trinotate.sh
#/bin/bash
TRINOTATE_HOME=/home/genektv/software/Trinotate-3.0.2
transcripts=../../Assembly/trinity_out_dir/Trinity.fasta
proteins=../step1_run_transdecoder/Trinity.fasta.transdecoder.pep
gene_trans_map=../../Assembly/trinity_out_dir/Trinity.fasta.gene_trans_map
Trinotate_sqlite=/home/genektv/database/Trinotate/Trinotate20170505.sqlite
blastp_outfmt6=../step2_run_blast_hmmer/blastp.outfmt6
blastx_outfmt6=../step2_run_blast_hmmer/blastx.outfmt6
pfam_out=../step2_run_blast_hmmer/TrinotatePFAM.out

#copy Trinotate.sqlite
cp $Trinotate_sqlite ./Trinotate.sqlite

#init
$TRINOTATE_HOME/Trinotate Trinotate.sqlite init --gene_trans_map $gene_trans_map --transcript_fasta $transcripts --transdecoder_pep $proteins

# load protein hits
$TRINOTATE_HOME/Trinotate Trinotate.sqlite LOAD_swissprot_blastp $blastp_outfmt6

# load transcript hits
$TRINOTATE_HOME/Trinotate Trinotate.sqlite LOAD_swissprot_blastx $blastx_outfmt6

# load pfam hits
$TRINOTATE_HOME/Trinotate Trinotate.sqlite LOAD_pfam $pfam_out

# report
$TRINOTATE_HOME/Trinotate Trinotate.sqlite report > trinotate_annotation_report.xls
```

```
/Annotation/Auto
/software/Trinotate/auto
pwd
cp /conf.txt ./
vi conf.txt#改软件地址transdecoder，diamond blastp,不用的删掉
改数据库路径，BLASTX_SPROT_TRANS:--db --threads 
RUN=F
http://www.genek.tv/course/63/task/844/show

autoTrinotate.sh

#!/bin/bash

cp /home/genektv/database/Trinotate/Trinotate20170505.sqlite Trinotate.sqlite

ln -s ../../Assembly/trinity_out_dir/Trinity.fasta Trinity.fasta

perl /home/genektv/software/Trinotate-3.0.2/auto/autoTrinotate.pl \
        --Trinotate_sqlite Trinotate.sqlite \
        --transcripts Trinity.fasta \
        --gene_to_trans_map ../../Assembly/trinity_out_dir/Trinity.fasta.gene_trans_map \
        --conf conf.txt \
        --CPU 4

nohup sh autoTrinotate.sh & #5min
```

<br>

## 数据挖掘 

```
/Data_Mining
Data_Mining.sh

TRINITY_HOME=/home/genektv/miniconda2/opt/trinity-2.4.0
PtR=$TRINITY_HOME/Analysis/DifferentialExpression/PtR
samples_file=../Assembly/sample.txt
genes_TMM_EXPR_matrix=../Quantification/genes.TMM.EXPR.matrix
$PtR --matrix $genes_TMM_EXPR_matrix --samples $samples_file --compare_replicates
$PtR --matrix $genes_TMM_EXPR_matrix --samples $samples_file --sample_cor_matrix
$PtR --matrix $genes_TMM_EXPR_matrix --samples $samples_file --indiv_gene_cor TRINITY_DN8111_c0_g1 --top_cor_gene_count 10 --min_rowSums 3 --gene_factors gene_factor.txt
#STEP BY STEP

```
--heatmap
data  transformation last3
clustering method cluster none
<br>

## 差异表达分析

```
/DE_analysis
conda install bioconductor-deseq2
R #进入命令模式
install.packages("DESeq2") #selection 15 (镜像不可用)

#载入安装工具
source("https://bioconductor.org/biocLite.R")

#安装包
biocLite("DESeq2")

#测试是否安装成功
library("DESeq2")
----------------------------
run_DE_analysis.sh
TRINITY_HOME=/home/genektv/miniconda2/opt/trinity-2.4.0
isoforms_counts_matrix=../Quantification/isoforms.counts.matrix
samples_file=../Assembly/sample.txt

perl $TRINITY_HOME/Analysis/DifferentialExpression/run_DE_analysis.pl \
        --matrix $isoforms_counts_matrix \
        --method edgeR \
        --samples_file $samples_file 
------------------------------
awk '($4>1 || $4<-1) && $7<0.05 && NR>1{print $1}' isoforms.counts.matrix.normal_vs_tumor.edgeR.DE_results >isoforms.counts.matrix.normal_vs_tumor.edgeR.DE.lst
--------------------------------------
```

<br>

## 富集分析

```
/GO #数据偏向性
conda install bioconductor-qvalue
vi run_GOSeq
#!/bin/bash

TRINITY_HOME=/home/genektv/miniconda2/opt/trinity-2.4.0/
TRINOTATE_HOME=/home/genektv/software/Trinotate-3.0.2/

################################
#差异基因列表
#使用 awk 命令提取得到
################################
de_lst=../DE_analysis/edgeR.3978.dir/isoforms.counts.matrix.normal_vs_tumor.edgeR.DE.lst 

################################
#从 Trinotate 结果中提取 GO 注释
#参数：-T isoform， -G gene 层次
################################
Trinotate_report=../Annotation/Auto/Trinotate.xls
perl ${TRINOTATE_HOME}/util/extract_GO_assignments_from_Trinotate_xls.pl \
        --Trinotate_xls $Trinotate_report \
        -T --include_ancestral_terms \
        > go_annotations.txt


################################
#长度信息
################################
transcript=../Assembly/trinity_out_dir/Trinity.fasta
perl ${TRINITY_HOME}/util/misc/fasta_seq_length.pl $transcript > trans.lengths.txt

#如果是 gene 层次，使用下面脚本计算得到
#perl $TRINITY_HOME/util/misc/TPM_weighted_gene_length.py \
#        --gene_trans_map ${transcript}.fasta.gene_trans_map \
#        --trans_lengths trans.lengths.txt \
#        --TPM_matrix isoforms.TMM.EXPR.matrix > genes.lengths.txt

#背景基因列表
background=../DE_analysis/edgeR.3978.dir/isoforms.counts.matrix.normal_vs_tumor.edgeR.count_matrix


perl ${TRINITY_HOME}/Analysis/DifferentialExpression/run_GOseq.pl \
        --genes_single_factor $de_lst \
        --GO_assignments go_annotations.txt \
        --lengths trans.lengths.txt \
        --background $background
#enrich depleted excel

ggplot,excel show imgs
```

