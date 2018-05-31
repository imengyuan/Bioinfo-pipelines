#! /usr/bin/env perl
# 分scaffold 生成gatk call snp的命令。
use strict;
use warnings;

my $now=$ENV{'PWD'};
my $dict="/data/part2/data/scaffold37_cov106.dict";
my $ref="/data/part2/data/scaffold37_cov106.fa";
my @bam=</data/part2/data/01.bam/*.bam>;
my $gatk = "/data/part2/software/GenomeAnalysisTK.jar";

open(O,"> bam.list");
foreach my $bam(@bam){
    $bam=~/([^\/]+)$/;
    my $name=$1;
    print O "$bam\n";
}
close O;


open(O,"> $0.sh");
open(S,"> $0.supp.sh");
open(I,"< $dict");

my $output_dir = "02.SNPbyChr";
`mkdir $output_dir` if (!-e $output_dir);

while(<I>){
    chomp;
    next unless(/SN:(\S+)\s+LN:(\d+)/);
    my ($chr,$len)=($1,$2);
    my $output_id= $chr;
    `mkdir $now/$output_dir/$output_id` if(!-e "$now/$output_dir/$output_id");
    print O "java -jar $gatk -T HaplotypeCaller -R $ref -I $now/bam.list -L $chr -o $now/$output_dir/$output_id/$output_id.vcf.gz\n";
    if(!-e "$now/$output_dir/$output_id/$output_id.vcf.gz.tbi"){
	print S "java -jar $gatk -T HaplotypeCaller -R $ref -I $now/bam.list -L $chr -o $now/$output_dir/$output_id/$output_id.vcf.gz\n";
    }
}

close I;
close O;
close S;
