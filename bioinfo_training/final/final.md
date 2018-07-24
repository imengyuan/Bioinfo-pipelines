##先把脚本传到服务器

# 得到物种名list
get_format_list.pl

# 批量写脚本
注意命名的前后缀
```shell
##
for i in /data/part2/00.bam/*bam;do samtools depth $i > ${i##*/}.depth;done
for i in *depth;do python3 avg_depth.py $i;done
for i in *sh;do sh $i;done
##
for i in *.fq.gz;do fq2psmcfa -q20 $i > ${i%.fq.gz}.psmcfa;done
for i in *.psmcfa;do psmc -N25 -t15 -r5 -p "4+25*2+4+6" -o ${i%.psmcfa}.psmc $i;done
for i in *.psmc;do psmc_plot.pl -g 10 ${i%.psmc} $i;done

```


for i in *.fst;do python3 avgfst.py $i >fst.value;done

# week14的
export PATH=$PATH:/data/part2/software/plink-v1.90/
export PATH=$PATH:/data/part2/software/vcftools_0.1.12b/bin/
export PATH=$PATH:/data/part2/software/admixture_linux-1.3.0/
export PATH=$PATH:/data/part2/software/treebest-1.9.2/

```shell
#test.list，记录scaffold37_cov106.vcf.gz中要用到的物种
# get test.recode.vcf
/data/part2/software/vcftools_0.1.12b/bin/vcftools --gzvcf scaffold37_cov106.vcf.gz --keep test.list --recode --recode-INFO-all --out test
# get gzip test.record.vcf.gz
gzip test.record.vcf
# get fresh.vcf.gz
0608new.pl test.record.vcf.gz fresh.vcf.gz

## 1PCA get fresh.eigenvec
/data/part2/software/plink-v1.90/plink --vcf fresh.vcf.gz --pca --allow-extra-chr --out fresh
#分裂数据，选取数据第一列与第二列、第一列与第三列作散点图，得到PCA图
08.pca.sh
plink --vcf scaffold4.vcf.gz --pca --allow-extra-chr --out outpca


## 2柱形图
# get out.bed out.bim
/data/part2/software/plink-v1.90/plink --vcf fresh.vcf.gz --allow-extra-chr --out fresh
# get new plink.bim
cp plink.bim plink.bim2
cat plink.bim2 | sed 's|scaffold37_cov106|1|g'>plink.bim
# get .Q
for ((i=1;i<11;i++));do /data/part2/software/admixture_linux-1.3.0/admixture --cv -j12 out.bed $i | tee out.bed.${i}.log;done   
#在第一列插入物种名，全部数据作堆积柱形图，调整线条百分比

09.structure.sh
perl 0608new.pl scaffold4.vcf.gz new.vcf.gz
plink --vcf new.vcf.gz --allow-extra-chr --out new
cp new.bim new.bim2
cat new.bim2 | sed 's|scaffold4_cov105|1|g'>new.bim
for ((i=1;i<5;i++));do admixture --cv -j12 new.bed $i | tee new.bed.${i}.log;done

## 3建NJ树 
/data/part2/software/plink-v1.90/plink --vcf fresh.vcf.gz  --make-bed --allow-extra-chr
# get plink.mdist plink.mdist.id
/data/part2/software/plink-v1.90/plink --bfile plink --allow-extra-chr --distance-matrix
# get plink.phylip
perl 204.pl
# get fresh.nj
/data/part2/software/treebest-1.9.2/treebest nj -b 100 plink.phylip > fresh.nj
# http://phylo.io，复制文件内容，查看模型
```
07.nj.sh
plink --vcf scaffold4.vcf.gz  --make-bed --allow-extra-chr
plink --bfile plink --allow-extra-chr --distance-matrix
perl get.phylip.pl
treebest nj -b 100 plink.mdist.phylip > tree.nj



# python读写文件
/day03/test001
单个文件
/day03/test002
多个文件
/day04
正则表达式

```python
# day03/test001 
#test001 total line numbers
count = len(open('01-The_Philosophers_Stone.txt','rU').readlines())
#test002 total word count
f = open('01-The_Philosophers_Stone.txt')
info = f.read()
alist = info.split(' ')  
word = len(alist)  
blankspace = alist.count('') 
print("total word count is ", word - blankspace)
f.close()
# test003 each word freguency
# test004 each character counts
# test005 how many empty lines
# test006 list distance between two words
# day03/test002 读取 *.txt 对每个txt文件输出上面各结果
```
## 写文件
```python
from itertools import product

src_list = ['A','B','C','D']
product = list(product(src_list, repeat=10))
string_list = []

f = open('test001.txt','w')
for term in product:
    p = "".join(list(term))
    string_list.append(p)
    f.write(p)
print(string_list)
```

杂合度
0.193285312773571
3 4写到一起

插入长度500bp
确认文件格式

01.get.list.sh
perl get_format_list.pl
cat 00.list.* > all.list
1 2 6789

3  每个个体的杂合度（计算公式：ref/alt位点数量  除以  no-miss的总位点数量）
4  每个物种的平均杂合度（该物种中所有个体杂合度的平均值）
5  每个物种的核酸多态性（pi）

03.het.sh
vcftools --gzvcf scaffold4.vcf.gz

04.species.het.sh
perl 04.peu.het.pl
perl 04.pil.het.pl
perl 04.PPr.het.pl