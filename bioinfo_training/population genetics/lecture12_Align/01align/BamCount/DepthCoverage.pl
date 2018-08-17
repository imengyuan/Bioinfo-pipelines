#!/usr/bin/perl -w
use strict;
my $ip_list = "01.bam.list";
my $op = $0.".count";
my $dict = "/tmpdata/train128/snp/scaffold37_cov106.dict";

open (D,"<$dict") or die ("$!\n");
<D>;
my $total_length;
while (my $eve = <D>){
    chomp($eve);
    my @a = split/\s+/,$eve;
    $a[2] =~ /LN:(\d+)/;
    my $scaffold_length = $1;
    $total_length += $scaffold_length;
}
close D;
open (I,"<$ip_list") or die ("$!\n");
open (O,">$op") or die ("$!\n");  
print O "id\ttotal_depth\tefficient_num\ttotal_length\n";
while (my $eve = <I>){
    chomp ($eve);
    $eve =~ /03.gatk\/(.+).realn.bam/;
    my $prefix = $1;
    open (F,"/data/part2/software/samtools-1.8/samtools depth $eve |");
    my $total_depth;
    my $efficient_num;
    #open (F,"<$ip") or die ("$!\n");
    #$ip =~ /02.op_depth\/(.+).depth/;
    #my $prefix = $1;
    while (my $tmp = <F>){
        chomp ($tmp);
        my @a = split/\s+/,$tmp;
        my $depth = $a[2];
        $total_depth += $depth;
        if ($depth > 0){
            $efficient_num++;
        }
    }
    close F;
    print O "$prefix\t$total_depth\t$efficient_num\t$total_length\t\n";
}

close I;
close O;

