#!/usr/bin/perl -w
use strict;

my $samtools = "/data/part2/software/samtools-1.8/samtools";
my $bcftools = "/data/part2/software/bcftools-1.8/bcftools";
my $ref = "/tmpdata/train128/snp/scaffold37_cov106.fa";
my $dict = "/tmpdata/train128/snp/scaffold37_cov106.dict";
my $bamList="01.bam.list";
my $vcf_dir = "02.vcf";
my $op = $0.".sh";
open (O,">$op") or die ("$!\n");
`mkdir $vcf_dir` if (! -e $vcf_dir);
open (F,"<$dict") or die ("$!\n");

while (my $eve = <F>){
    chomp($eve);
#SN:scaffold23.1
    next unless ($eve =~ (/SN:(scaffold\S+)/));
    my $chr=$1;
    print O "$samtools mpileup -A -ug -t DP -t SP -t DP4 -f $ref -r $chr -b $bamList | $bcftools call -vmO z -o $vcf_dir/$chr.vcf.gz\n";
}

close O;
