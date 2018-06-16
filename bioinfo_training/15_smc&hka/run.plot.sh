for i in *.fq.gz;do fq2psmcfa -q20 $i > ${i%.fq.gz}.psmcfa;done
for i in *.psmcfa;do psmc -N25 -t15 -r5 -p "4+25*2+4+6" -o ${i%.psmcfa}.psmc $i;done
for i in *.psmc;do psmc_plot.pl -g 10 ${i%.psmc} $i;done
