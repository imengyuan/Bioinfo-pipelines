/home/test-2018/train128/part1/velvet_1.2.10/velveth outdata 31 -fastq -shortPaired -separate read.1.fq.gz read.2.fq.gz

/home/test-2018/train128/part1/velvet_1.2.10/velvetg outdata -clean yes -exp_cov 21 -cov_cutoff 2.81 -min_contig_lgth 500

cp outdata/contigs.fa test008.fasta

./VelvetOptimiser.pl -s 33 -e 41 -f '-fastq -shortPaired -separate /home/train128/software/velvet/SRR292770_1.fastq /home/train128/software/velvet/SRR292770_2.fastq' -o '-min_contig_lgth 200' -p SRR292770

Final graph has 1941 nodes and n50 of 41355, max 146159, total 5302945, using 9193354/10204082 reads
