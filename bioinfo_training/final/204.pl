use strict;
use warnings;

open(F1,"plink.mdist");
open(F2,"plink.mdist.id");
open(O,">plink.mdist.phylip");


my @id;
while(<F2>){
	chomp;
	my @a=split(/\s+/,$_);
	#push @id,$a[0];
	my $idlength=length($a[0]);
	if ($idlength<10){
		my $fill= 10-$idlength;
		$a[0]=$a[0].(" " x $fill);
	}
	#print O ("$a[0]\n");
	push @id,$a[0];
}

my $len=scalar(@id);
print O ("\t$len\n");

my $count=0;
while (<F1>){
	chomp;
	print O ("$id[$count]\t$_\n");
	$count++;
}
close(F2);
close(O);
close(F1);