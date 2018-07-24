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
		next if($a[2] eq "mis");
		if($a[2] eq "ref/alt"){
			$K++
	
		}else{
			if($a[2] eq "ref" ){
				$D++;
			}elsif($a[2] eq "alt" ){
				$D++;
			}
		}
	}
}
close(F);
$answer=$K/($K+$D);
print"PPr杂合度为: $answer";


