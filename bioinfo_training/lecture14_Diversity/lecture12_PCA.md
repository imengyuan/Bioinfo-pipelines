# Population Structure


把第一列替换为1
```shell
cat plink.bim2 | sed 's|scaffold37_cov106|1|g'>new.plink.bim
```
未解决的问题：这里error read bed files
运行admixture
```shell
for ((i=1;i<11;i++));do /data/part2/software/admixture_linux-1.3.0/admixture --cv -j12 out.bed $i | tee out.bed.${i}.log;done
```

## PCA图ok
scaffold37_cov106.eigenval可用Excel打开，选取数据第一列与第二列、第一列与第三列作散点图，得到PCA图（>横PC1 纵PC3 >横PC1 纵PC2）。
## structure ok
在Excel下打开.Q，在第一列插入物种名，利用各列数据作堆积柱形图。
## NJ树 ok
登录http://phylo.io，上传fresh.nj文件，查看得到的进化树模型。
## Fst
用Excel打开6个fst文件，查找替换掉无效值，计算剩余fst平均值，并建表统计


###filter.pl
Quality Filter: 7875
Multi Allele: 0
Non SNP:116130
SNP: 136250
0	8060
1	11789
2	11045
3	8745
4	6929
5	5688
6	5150
7	4751
8	4515
9	4262
10	4998
11	5337
12	5405
13	5378
14	5178
15	5140
16	5033
17	5090
18	4970
19	4963
20	5102
21	4690
22	4032


/data/part2/software/vcftools_0.1.12b/bin/vcftools --vcf output.vcf  --weir-fst-pop peu.txt --weir-fst-pop ppr.txt  --out peu_ppr.fst
/data/part2/software/vcftools_0.1.12b/bin/vcftools --vcf output.vcf  --weir-fst-pop peu.txt --weir-fst-pop pil.txt  --out peu_pil.fst
/data/part2/software/vcftools_0.1.12b/bin/vcftools --vcf output.vcf  --weir-fst-pop peu.txt --weir-fst-pop ptr.txt  --out peu_ptr.fst
/data/part2/software/vcftools_0.1.12b/bin/vcftools --vcf output.vcf  --weir-fst-pop ppr.txt --weir-fst-pop pil.txt  --out ppr_pil.fst
/data/part2/software/vcftools_0.1.12b/bin/vcftools --vcf output.vcf  --weir-fst-pop ppr.txt --weir-fst-pop ptr.txt  --out ppr_ptr.fst
/data/part2/software/vcftools_0.1.12b/bin/vcftools --vcf output.vcf  --weir-fst-pop pil.txt --weir-fst-pop ptr.txt  --out pil_ptr.fst


[train128@train2018]~/week14-new/new% cat *.log | grep CV
CV error (K=10): 0.38541
CV error (K=1): 0.99183
CV error (K=2): 0.51576
CV error (K=3): 0.22660
CV error (K=4): 0.17662
CV error (K=5): 0.20110
CV error (K=6): 0.22979
CV error (K=7): 0.24047
CV error (K=8): 0.32271
CV error (K=9): 0.28246