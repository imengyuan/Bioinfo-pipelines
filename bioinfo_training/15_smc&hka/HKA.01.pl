use strict;
use warnings;

my $file="scaffold37_cov106.vcf.gz";
my @head; #记录表头文件
my %species;
my @species; #记录物种名
open(F,"zcat $file |");
open(O,'>',"HKA.01.pl.out");

while(<F>){
	chomp;
	next if(/^##/);
	if(/^#/){
		@head=split(/\s+/,$_);
		for (my $i=9;$i<@head;$i++){
			$head[$i]=~m/(\S+)\d\d/;
			my $species=$1;
			$species{$species}++;
		}
		@species=sort(keys %species); 
		print O "#scaffold\tPos\t",join("\t",@species),"\n";
	}else{
		my @a=split(/\s+/,$_);
		my $scaffold=$a[0];
		my $Pos=$a[1];
		my %genotype;
		for(my $i=9;$i<@a;$i++){
			$head[$i]=~m/(\S+)\d\d/;
			my $species=$1;
			if($a[$i]=~m/0\/0/){
				$genotype{$species}{ref}++;
			}elsif($a[$i]=~m/0\/1/){
				$genotype{$species}{ref}++;
				$genotype{$species}{alt}++;
			}elsif($a[$i]=~m/1\/1/){
				$genotype{$species}{alt}++;
			}else{
				
			}
			
		}
		print O "$scaffold\t$Pos";
		foreach my $species(@species){
			my $print="mis";
			if(exists $genotype{$species}){
				my @tmp=keys %{$genotype{$species}};
				if(scalar(@tmp)==2){
					$print="het";
				}else{
					$print=$tmp[0];
				}
			}
			print O "\t$print";
		}
		print O "\n";
	}
}
close (O);
close (F);