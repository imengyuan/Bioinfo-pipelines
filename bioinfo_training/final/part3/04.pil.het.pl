use strict;
use warnings;

open(F,"02.HKA.out");
my @head;
my $D=0;
my $K=0;
my $answer=0;
while(<F>){
	chomp;
	if (/^#/) {
		@head=split(/\s+/,$_);
	}else{
		my @a=split(/\s+/,$_);
		next if($a[4] eq "mis");
		if($a[4] eq "ref/alt"){
			$K++
	
		}else{
			if($a[4] eq "ref" ){
				$D++;
			}elsif($a[4] eq "alt" ){
				$D++;
			}
		}
	}
}
close(F);
$answer=$K/($K+$D);
print"pil杂合度为: $answer";


