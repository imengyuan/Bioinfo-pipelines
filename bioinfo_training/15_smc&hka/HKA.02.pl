use strict;
use warnings;

open(F,"HKA.01.pl.out");
my @head;
my $D=0;
my $K=0;
while(<F>){
	chomp;
	if (/^#/) {
		@head=split(/\s+/,$_);
	}else{
		my @a=split(/\s+/,$_);
		next if($a[2] eq "mis");
		if($a[2]=~m/het/){
			$K++;#统计多态位点
		}else{
			if($a[2] eq "ref" && $a[4] eq "alt"){#目标和外类群
				$D++;
			}elsif($a[2] eq "alt" && $a[4] eq "ref"){
				$D++;
			}
		}
	}
}
close(F);
print "PPr: $D fixed: $K poly\n";

#32281 54575
