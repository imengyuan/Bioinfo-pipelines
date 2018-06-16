import sys

filein=open(sys.argv[1],'r')
line=filein.readline()
sum_d=0
count=0
while line:
	sum_d+=int(line.rstrip().split("\t")[2])
	count+=1
	line=filein.readline()
filein.close()

avg_d=sum_d/count

fileout=open(sys.argv[1][:-5]+"sh","w")
print(r'samtools mpileup -C50 -uf /tmpdata/train128/05.psmc/scaffold37_cov106.fa /data/part2/00.bam/{0} | bcftools call -c - \ | vcfutils.pl vcf2fq -d {1} -D {2} | gzip > diploid_{0}.fq.gz'.format(sys.argv[1][:-6],avg_d/3,avg_d*2),file=fileout)
fileout.close()

