# 基因组数据处理和分析基本流程


## 基本流程
* 样品设计-收集/处理样品-提取DNA-建库测序
* 质控-组装-基因结构与功能注释
* 基因家族分析-扩张/收缩-系统发育-Selection-GO/KEGG
* 基因功能-PCR-E coli-cell culture-Mouse

1. 样品设计
 数量、生长发育阶段、性别、取样部位；特殊处理（去除肠道、多培养几代）？混合样品？

注释
## 重复注释
三种方案
* 从头预测
* 同源比对
* 基于RepeatProtein

1. 基于repeatmasker搜索重复序列
```shell
cd /data/project/gene_annatation/struction_annatation/Repeat

ln –s ../test.fa

echo “/data/project/tools/RepeatMasker/RepeatMasker -engine ncbi -nolow -lib /data/project/tools/RepeatMasker/Libraries/RepeatMaskerLib.embl.lib –xsmall test.fa” >>repeatmasker.sh

qsub –l vf=5G,p=5 -l h=roach –cwd –S /bin/bash repeatmasker.sh
```

2. 基于repeatprotein搜索重复序列
```
echo “/data/project/tools/RepeatMasker/RepeatProteinMask -noLowSimple -pvalue 1e-4 test.fa” >>repeatprotein.sh

qsub –l vf=5G,p=5 -l h=roach –cwd –S /bin/bash repeatprotein.sh
```

3. 基于trf搜索重复序列
```
echo /data/project/tools/RepeatMasker/trf test.fa  2 7 7 80 10 50 2000 -d –h” >>repeat trf.sh

qsub –l vf=5G,p=5 -l h=roach –cwd –S /bin/bash repeat trf.sh
```

4. 重复序列屏蔽
```
cd /data/project/gene_annatation/struction_annotation 

cat  *.gff >>repeat.gff

perl /data/project/jjz/dalian/5.repeatmask/denovo/soft_mask_by_gff.pl test.fa  repeat.gff
 >>test_repeat.fa
```


## 结构注释
三种方式
* 从头预测
* 基于蛋白质的同源预测
* 基于转录组的预测
所有的注释结果最后利用EVM或者GLEAN的方式进行整合，最终得到可靠的基因区域
![]()

常用于De novo 预测的软件有： Augustus、Glimmer、Genscan、GeneMark、SNAP等。

1. Augustus
```
cd /data/project/gene_annatation/struction_annatation/AUGUSTUS

ln –s ../test.fa

/data/project/tools/augustus-3.2.1/bin/augustus --strand=both --singlestrand=false --protein=on --introns=on --start=on --stop=on --cds=on --codingseq=on  --gff3=on --outfile= /data/project/gene_annatation/struction_annatation/AUGUSTUS/Augustus.gff --species=chicken  test.fa

grep  ‘^scaffold’ Augustus.gff  >>Augustus.gff3
```

2. Genscan
```
cd /data/project/gene_annatation/struction_annatation/GENESCAN

ln –s  ../test.fa

nohup perl /data/project/tools/Genscan/genscan_pip/Genscanpip.pl -f test.fa -t 7000000 -s HumanIso.smat -d /data/project/tools/Genscan -l &
ln –s  /data/project/gene_annatation/struction_annatation/GENESCAN/genscan.out/total.fa.genscan.gff
```

3. SNAP
```
cd /data/project/gene_annatation/struction_annatation/SNAP

ln –s ../test.fa

/data/project/jjz/soft/snap/snap -lcmask  -gff /data/project/jjz/dalian/3.genpredict/denovo/ snap/mam54.hmm test.fa >> snap.gff 
awk 'BEGIN{OFS="\t"}{$3="CDS";$6="";$9="Name="$9;print }' snap.gff > snap.gff3

perl /data/project/tools/EVidenceModeler-1.1.1/EvmUtils/misc/SNAP_to_GFF3.pl snap.gff3 > snap.evm.gff3
```

## 功能注释
![]()

* Experiment
Prokaryotic expression，knock down, know off in model organisms …
* Public databases
    1. GO: [Gene Ontology](http://www.geneontology.org/)
    2. KEGG: Kyoto Encyclopedia of Genes and Genomes
    3. Uniprot: Universal protein Swiss-Prot+TrEMBL+PIR-PSD 
    4. Interpro: Protein sequence analysis & classification

将所有注释到的基因提取到蛋白质序列，将这些蛋白质基因桶过blast与各个蛋白质数据库相比对。最终得到基因的注释信息。

几个数据库
### GO three top roots
* molecular function
molecular activities of gene products: the tasks preformed by individual gene products; carbohydrate binding, ATPase activity
* cellular component
where gene products are active: Subcellular structures, locations, and macromolecular complexes; nucleus, telomere, RNA polymerase II holoenzyme
* biological process
pathways and larger processes made up of the activities of multiple gene products: broad biological goals; mitosis or purine metabolism, that are accomplished by ordered assemblies of molecular functions

### KEGG pathway [](http://www.genome.jp/kegg/)
A series of actions among molecules in a cell that leads to a certain product or a change in a cell.

### UniProt [](http://www.uniprot.org)
### InterProt [](https://www.ebi.ac.uk/interpro/)

### 操作
1. NR数据库
```
cd /data/project/gene_annatation/function_annatation/NR

ln –s ../test.pep.fa

echo “/data/project/tools/ncbi-blast-2.2.28+/bin/blastp  -evalue 1e-5 -outfmt 6  -db /data/project/blastdb/nr/20171102/nr  -query test.pep.fa
 –out nr.tab -num_threads 3 -max_target_seqs 1” >>nr.sh

qsub –l vf=3,p=3 –l h=roach –cwd –S /bin/bash nr.sh
```

2. Swiss-prot
```
cd /data/project/gene_annatation/function_annatation/Swiss-prot

ln –s ../test.pep.fa

echo “/data/project/tools/ncbi-blast-2.2.28+/bin/blastp  -evalue 1e-5 -outfmt 6  -db /data/project/blastdb/swissprot/swissprot -query test.pep.fa
 –out swissprot.tab -num_threads 3 -max_target_seqs 1” >>swissprot.sh

Qsub –l vf=3,p=3 –l h=roach –cwd –S /bin/bash swissprot.sh
```

3. TrEMBL
```
cd /data/project/gene_annatation/function_annatation/TrEMBL

ln –s ../test.pep.fa

echo “/data/project/tools/ncbi-blast-2.2.28+/bin/blastp  -evalue 1e-5 -outfmt 6  -db /data/project/blastdb/TrEMBL/TrEMBL  -query test.pep.fa –out TrEMBL.tab -num_threads 3 -max_target_seqs 1”

qsub –l vf=3,p=3 –l h=roach –cwd –S /bin/bash swissprot.sh
```

4. interproscan
```
cd /data/project/gene_annatation/function_annatation/interproscan

ln –s ../test.pep.fa

echo “/data/project/tools/interproscan-5.18-57.0/./interproscan.sh  -iprlookup  -pa -goterms –i test.pep.fa –b test.pep.fa” >>interproscan.sh

nohup sh interproscan.sh &
```





