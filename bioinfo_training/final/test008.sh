./velveth outdata 31 -fastq -shortPaired -separate SRR292770_1.fastq SRR292770_2.fastq

./velvetg outdata2 -clean yes -exp_cov 21 -cov_cutoff 2.81 -min_contig_lgth 200

Final graph has 1941 nodes and n50 of 41355, max 146159, total 5302945, using 9193354/10204082 reads

cp outdata/contigs.fa SRR292770_unordered.fasta

./VelvetOptimiser.pl -s 33 -e 41 -f '-fastq -shortPaired -separate /home/train128/software/velvet/SRR292770_1.fastq /home/train128/software/velvet/SRR292770_2.fastq' -o '-min_contig_lgth 200' -p SRR292770