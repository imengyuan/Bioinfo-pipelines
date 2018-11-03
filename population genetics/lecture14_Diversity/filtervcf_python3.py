import gzip
import os
import re

infile = gzip.GzipFile("4species.vcf.gz", "r")
filtered_data=[]
line=str(infile.readline())
line=line[2:-1]
line=line.replace("\\n","")
multi=0
quality=0
snp=0
nsnp=0
miss=0
miss_record=[]
while line:
	if line[0:2]!="##":
		if line[0]=="#":
			record=line.split("\\t")
			filtered_data.append("\t".join(record))
		else:
			flag=1
			record=line.split("\\t")
			if record[4]==',' or len(record[4])>1:
				flag=0
				multi+=1
			if float(record[5])<100:
				flag=0
				quality+=1
			summary=[]
			miss_N=0
			for i in record[9:]:
				if i!="./.":
					summary.append(i[0])
					summary.append(i[2])
				else:
					miss_N+=1
			N_REF=summary.count("0")
			N_VAR=summary.count("1")
			if N_REF<1 or N_VAR<1:
				flag=0
				nsnp+=1
			if miss_N>23:
				flag=0
				miss+=1
			if flag==1:
				string="\t".join(record)
				filtered_data.append(string)
				snp+=1
				miss_record.append(miss_N)
	else:
		filtered_data.append(line)
	line=str(infile.readline())
	line=line[2:-1]
	line=line.replace("\\n","")
fileout=open("4_species_filtered.vcf","w")
for i in filtered_data:
	print(i,file=fileout)
fileout.close()
print("bad quality ",quality)
print("no multi ALLELE ",multi)
print("snp ",snp)
print("none-snp ",nsnp)
print("miss ",miss)
for i in range(0,20):
	print(i,"\t",miss_record.count(i))



