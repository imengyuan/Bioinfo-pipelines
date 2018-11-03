use strict;
use warnings;

my $file="scaffold37_cov106.vcf.gz";
my %species;
my %species1;
open(F,"zcat $file |") || die  "$file open failed/n";
while(<F>){
	chomp; #把换行符删掉
	if(/^##/){
		next;
	}
	elsif(/^#/){
		my @a=split(/\s+/,$_);  #定义一个数组a将第一行匹配用空行分开
		for (my $i=9;$i<@a;$i++){
			my $individual=$a[$i];
			if($individual =~m/(\S+)\d\d/){
				my $tmp=$1;
				$species{$tmp}{$individual}++;
				push @{$species1{$tmp}},$individual;
			}else{
				die "$individual can not match\n";
			}
		#	print "$a[$i]\n";
		}
		last;
	}
}
close(F);

foreach my $tmp(keys %species){
	open(O,">00.list.$tmp");
	my @individual=keys %{$species{$tmp}};
	print O join("\n",@individual),"\n";
	close(O);

}

#foreach my $tmp(keys %species1){	
        #open(O,">01.list.$tmp.1");
   #     my @individual=keys @{$species1{$tmp}};
  #      print O join("\n",@individual),"\n";
 #       close(O);
#}

