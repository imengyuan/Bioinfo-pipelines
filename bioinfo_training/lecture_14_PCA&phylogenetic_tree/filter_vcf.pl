use strict;
use warnings;

my($input,$out)=@ARGV;
open(F,"zcat $input |") || die "input\n";
open(O,"| gzip - >$out") || die "$out\n";
my $quality = 0;
my $multiAllele = 0;
my $NonSNP = 0;
my $snp=0;
my %miss;
while(<F>){
	chomp;
	if(/^#/){
		print O "$_\n"
	}else{
		my @a = split(/\s+/,$_);
		if($a[5]<100){
			$quality++;
			next;
		}elsif($a[4]=~m/,/ || length($a[4])>1){
			$multiAllele++;
			next;
		}else{
			my $ref=0;
			my $alt=0;
			my $miss=0;
			for(my $i=9;$i<@a;$i++){
				if($a[$i]=~m/0\/0/){$ref+=2;}
				if($a[$i]=~m/0\/1/){$ref++;$alt++;}
				if($a[$i]=~m/1\/1/){$alt+=2;}
				if($a[$i]=~m/\.\/\./){$miss++;}
				}
				if($ref>0 && $alt>0 && $miss<23){
					$miss{$miss}++;
					print O "$_\n";
					$snp++;
				}else{
					$NonSNP++;
					next;
				}
			}
		}
 }
close(F);
close(O);
print "Quality Filter: $quality\nMulti Allele: $multiAllele\nNon SNP:$NonSNP\nSNP: $snp\n"; 
foreach my $miss(sort{$a<=>$b}(keys %miss)){
	print "$miss\t$miss{$miss}\n";
}

 	