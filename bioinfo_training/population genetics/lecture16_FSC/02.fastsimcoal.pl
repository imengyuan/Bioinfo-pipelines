#! /usr/bin/env perl
use strict;
use warnings;

my $fsc="/data/part2/software/fsc_linux64/fsc25221";

my $dir=$ENV{'PWD'};
`mkdir $dir/replicates` if(!-e "$dir/replicates");
open(O,"> run.sh");
for(my $i=1;$i<=10;$i++){
    my $cmd="$fsc -t model.tpl -n100000 -N100000 -m -s 0 -e model.est -M 0.001  -l 10 -L 40 -c 6 -q";
    my $tmpdir="$dir/replicates/run$i";
    `mkdir $tmpdir`;
    `cp *.obs $tmpdir; cp model.tpl model.est $tmpdir;`;
    print O "cd $tmpdir; $cmd\n";
}
