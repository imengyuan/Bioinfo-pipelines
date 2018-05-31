use strict;
use warnings;
my $file=shift;

open(F,"zcat $file |")||die "$file not exist\n";
open(O,'>',"$file.filter");
while(my $line=<F>){
    chomp;
    if($line=~m/^#/){
        print O "$line\n";
    }else{
        my @line=split(/\s+/,$line);
        if(%line[5]>=30){
        print O "$line\n";}
    }
}
