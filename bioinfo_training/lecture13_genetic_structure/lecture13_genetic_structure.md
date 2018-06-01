# genetic structure of a population

<br>

## 一些概念
### Two Types

1. alleles
2. genotypes

Some Concepts:

* frequency
* Hardy-Weinberg principle(卡方检验)
    * allele frequency will not change
    * heterozygotes has higher frequency

### Question of Interest

* patterns of genetic variation in population
* change in genetic structure through time

Genetic Variation:

* SNP
* indel
* SV

<br>



## Vcftools的使用

* [Mannual地址](http://vcftools.sourceforge.net/man_latest.html) 
* vcf格式文件的介绍 vcf.formate

### 计算等位基因频率

```shell
# 计算各位点的等位基因频率
vcftools --gzvcf scaffold37_cov106.vcf.gz --out 01.list --freq
# -out: prefix, --freq: fuction 
# output: 01.list.frq
```
输出01.list.frq截图为frq_output_screeshot.png

可以自己写一个脚本算等位基因频率，参考get_frq.py

<br>

### 计算其他参数值

```shell
vcftools --gzvcf scaffold37_cov106.vcf.gz --out new.list <argument>
# --window-pi 3023989 计算pi值
#--TajimaD 3023989 计算TajimaD值，后面接window-size值用的是contig的长度
#--chr scaffold37_cov106 --LROH 计算ROH值
#--het 计算杂合度
```
这里计算pi值也可以自己接着get_frq.py写计算pi值的脚本get_pi.py

限制物种的参数
```
--keep <name_list_file>
```

从原始vcf.gz文件中获取每个物种的不同个体名单，参考get_format_list.pl和没写完的get_format_list.py

<br>

### 批量计算生成表格
根据get_format_list.pl生成的名称list作为--keep的参数，对每个物种分别计算pi，TajimaD，LROH和het杂合度。

批量生成脚本all.sh
```shell
for file in ./00.list.*;do /data/part2/software/vcftools_0.1.12b/bin/vcftools --gzvcf scaffold37_cov106.vcf.gz --out ${file#*.} --window-pi 3023989 --keep $file;done

for file in ./00.list.*;do /data/part2/software/vcftools_0.1.12b/bin/vcftools --gzvcf scaffold37_cov106.vcf.gz --out ${file#*.} --TajimaD 3023989 --keep $file;done

for file in ./00.list.*;do /data/part2/software/vcftools_0.1.12b/bin/vcftools --gzvcf scaffold37_cov106.vcf.gz --out ${file#*.} --LROH --chr scaffold37_cov106  --keep $file;done

for file in ./00.list.*;do /data/part2/software/vcftools_0.1.12b/bin/vcftools --gzvcf scaffold37_cov106.vcf.gz --out ${file#*.} --het  --keep $file;done

```

提取结果生成表格(table.jpg)使用get_table_new.py

## 总结
python写脚本还是多多练习吧...






