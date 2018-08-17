import gzip
import os
import re

infile = gzip.GzipFile("../scaffold37_cov106.vcf.gz", "r")
out_data=[]
line=str(infile.readline())
line=line[2:-1]
line=line.replace("\\n","")
while line:
	if line[0:2]!="##":
		record=line.split("\\t")
		record=record[:19]+record[25:35]+record[46:72]
		out_data.append("\t".join(record))
	else:
		out_data.append(line)
	line=str(infile.readline())
	line=line[2:-1]
	line=line.replace("\\n","")
infile.close()
outfile=open("4species.vcf","w")
for i in out_data:
	print(i,file=outfile)
outfile.close()

	

