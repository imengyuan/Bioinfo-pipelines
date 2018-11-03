my ($vcf1,$vcf2)=@ARGV;
my %pos1;

open(F,"zcat $vcf1 |");
while(<F>){
    chomp $_;
    next if($_=~/^#/);
    my @a=split(/\s+/,$_);
    my $scaffold=$a[0];
    my $pos=$a[1];
    $pos1{$scaffold}{$pos}++;
}
close(F);


my %pos2;
my $overlap=0;
open(F,"zcat $vcf2|");
while(<F>){
    chomp;
    next if(/^#/);
    my @a=split(/\s+/,$_);
    my $scaffold=$a[0];
    my $pos=$a[1];
    $pos2{$scaffold}{$pos}++;
    if(exists $pos1{$scaffold}{$pos}){
	$overlap++;
    }
}
close(F);

foreach my $scaffold(keys %pos1){
    my @pos=keys %{$pos1{$scaffold}};
    foreach my $pos(@pos){
	if($pos1{$scaffold}{$pos}>1){
	    print "$scaffold\t$pos\n";
	}
    }
}

##
foreach my $scaffold(sort(keys %pos1)){
    print "$vcf1\t$scaffold\t",scalar(keys(%{$pos1{$scaffold}})),"\n";
    print "$vcf2\t$scaffold\t",scalar(keys(%{$pos2{$scaffold}})),"\n";
}
print "overlapSites: $overlap\n";
##
