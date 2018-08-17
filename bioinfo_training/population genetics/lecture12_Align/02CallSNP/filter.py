import re 
f = open('zcat 02.vcf/scaffold37_cov106.vcf.gz |')
lines = f.readlines()
for line in lines:
    if re.match('^\#(.*)', line):
        print(line)
    else:
        line.split()
        print(line)
