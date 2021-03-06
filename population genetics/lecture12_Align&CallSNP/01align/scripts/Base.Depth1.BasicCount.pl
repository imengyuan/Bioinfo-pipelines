#!/usr/bin/perl -w
#此脚本计算了每一个深度下对应的碱基数目，需要将$path改为自己的samtools的路径
#基因组fasta文件 bam文件 输出文件
use strict;
use Bio::SeqIO;
my $path = "/data/part2/software/samtools-1.8/samtools";
my $fasta = "/tmpdata/train128/snp/scaffold37_cov106.fa";
my $bam = "/tmpdata/train128/snp/03.gatk/*.bam";
my $op = "output.depth1";
my %hash;
open (O,">$op") ||die ("$!\n");
my $fa = Bio::SeqIO->new(-file=>$fasta, -format=>'fasta');
while(my $seq= $fa->next_seq){
    my $id = $seq->id;
    my $seq = $seq->seq;
    open (I,"$path depth -r $id $bam |");
    while(my $eve = <I>){
	chomp ($eve);
	my @infor = split/\t/,$eve;
	my $depth = $infor[2];
	$hash{$depth}++;
    }
    close I;
}
foreach my $depth (sort {$a<=>$b} keys %hash){
    print O "$depth\t$hash{$depth}\n";
}
close O;
