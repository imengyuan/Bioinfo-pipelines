# Geneious的使用 | 以组装注释并提交叶绿体基因组为例

<br>

## 安装、申请免费试用与基本操作

<br>

### 安装与免费使用

![](https://github.com/ViciaYuan/Bioinfo-pipelines/tree/master/cpg-analysis/1geneious.jpg)

在官网 https://www.geneious.com/ 上下载安装，并申请free trial（实验室买了license另说...）。免费试用期有14天...过了要么只能用restricted的版本（几乎没什么功能），要么在虚拟机上的新系统上重复“安装-免费使用14天”的过程。记得分配好geneious运行所需的磁盘和内存大小，不然带不动。


<br>

### 基本操作

![](https://github.com/ViciaYuan/Bioinfo-pipelines/tree/master/cpg-analysis/2support.jpg)

官网support这一栏 https://support.geneious.com/hc/en-us  提供了丰富的支持。

* Knowledge Base: 有分了类的常见问题
* Tutorial: 下载相应的教程，导入到geneious里能一步一步跟着做，可以快速入门一下各种操作
* Manual: 也可以自己查着用
* Contact Support: 实在没有搜到自己遇到问题的解答，登录提交一个问题，小半天能收到回复

在主页面上方点击Help(带问号的图标)，会在页面最右侧出现一个隔开的窗口，点击里面Tutorial，可以熟悉Geneious的用户界面、文件相关、NCBI搜索、序列查看与编辑、使用功能等的介绍。可以很快熟悉Geneious的基本使用。

![](https://github.com/ViciaYuan/Bioinfo-pipelines/tree/master/cpg-analysis/3interface.jpg)

1是菜单（menu），2是工具栏（tool bar），3是本地文件，4是从NCBI等上面搜索下载的文件，5是文件列表，6文件查看和编辑区，7查看内存的使用，点击可以回收一部分没在使用的内存。

有目的但不知道怎么操作的时候，多看下Tutorial和查Manual，自己折腾一下怎么用，资源还是挺丰富的。

<br>

## Map to Reference 比对到参考序列

<br>

1. 上面示意图的2为tool bar，选中需要map的序列，然后tool bar-> Align/Assemble-> Map to Reference,在弹出的窗口里选择参考序列，即可进行map
2. 产生的结果为一条Nucleotide alignment文件，选择tool bar-> Workflows-> merge mapped sequences，生成一条fasta序列
3. 选中生成的fasta文件，在6文件查看编辑区选择Info可以修改该序列的信息：Name, Common Name, Genetic Code, Organism, Topology 等。

这时候在Sequence View可以看到环状的叶绿体基因组序列（Info里改Topology为circular），没有注释的信息，下一步可以将参考序列的注释信息复制到我们的序列上去。

<br>

以下 **Transfer Annotations**和 **Submit to Genbank**都有对应的Tutorial文件，可以自己过一遍体会一下，这里作简单介绍。

<br>

## Transfer Annotations 复制参考序列的注释信息

有三种Transfer Annotations的方法。
* “Copy To”: 通过比对。转移短的单个注释，或用于整个序列有同源性的短的比对
* "Annotate From": 通过同源性。使用custom feature数据库，适用于注释有不同feature的未比对的序列
* "Transfer Annotation": 通过同源性。在比对或组装中，转移到参考序列或consensus序列，同源性存在于整个或一些比对。

三种方法是互补的，根据序列间同源性的情况和是否有注释好的参考序列来选择合适的方法。另外，三种方法的效果与比对情况有关，在所有注释的边界都应该再次确认他们是否正确，必要时可以调整注释的范围。


 “Copy To”
1. 安装MAFFT多序列比对插件：Menu-> Tools-> Plugins...-> Install Mafft Multiple Alignment Plugin
2. 比对：选中参考序列+待注释序列-> Tool bar-> Align/Assemble-> Pairwise/Multiple Align-> MAFFT Alignment-> ok
3. 复制注释：选中生成的Nucleotide alignment文件-> 点击参考序列右键-> Annotation-> Copy all in selected region to-> 待注释序列
4. 保存：选择save并应用到原始序列
5. 修正注释
    
"Annotate From"
1. 准备有注释文件的数据库，已有的或者自己创建
2. 在文件查看和编辑区右侧选择橙色带问号图标Live Annotate & Predict-> Annotate from-> Source选择数据库-> 调整Similarity的百分值-> Apply
3. 修正注释

"Transfer Annotation"
1. 和“Copy To”一样的比对得Nucleotide alignment文件-> 选中待注释序列右键-> Set as reference sequence
2. 和"Annotate From"一样选择Live Annotate & Predict-> Transfer Annotations调整Similarity的百分值-> Apply
3. 修正注释
<br>

## Submit to Genbank 提交

<br>
