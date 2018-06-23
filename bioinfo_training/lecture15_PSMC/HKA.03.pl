use strict;
use warnings;

open(F,"HKA.01.pl.out");
my @head;
my $D=0;
my $K=0;
my %wind;
my $scaffold;
while(<F>){
	chomp;
	if (/^#/) {
		@head=split(/\s+/,$_);
	}else{
		my @a=split(/\s+/,$_);
		next if($a[2] eq "mis");
		my $pos=$a[1];
		$scaffold=$a[0];
		
		my $wind=int($pos/10000)+1;
		if($a[2]=~m/het/){
			$K++;#统计多态位点
			$wind{$wind}{K}++;
		}else{
			if($a[2] eq "ref" && $a[4] eq "alt"){#目标和外类群
				$D++;
				$wind{$wind}{D}++;
			}elsif($a[2] eq "alt" && $a[4] eq "ref"){
				$D++;
				$wind{$wind}{D}++;
			}
		}
	}
}
close(F);
#print "PPr: $D fixed: $K poly\n";
open(O,'>',"HKA.03.pl.out");
print O "#scaffold\tstart\tend\tD\tK\tGenomeD\tGenomeK\n";
my @wind=sort{$a<=>$b}(keys %wind);
for(my $i=0;$i<@wind;$i++){
	print O "scaffold\t",($wind[$i]-1)*10000+1,"\t",$wind[$i]*10000,"\t";
	my $windD=0;
	my $windK=0;
	$windD=$wind{$wind[$i]}{D} if(exists $wind{$wind[$i]}{D});
	$windK=$wind{$wind[$i]}{K} if(exists $wind{$wind[$i]}{K});
	print O "$windD\t$windK\t$D\t$K\n";
}
close(O);


