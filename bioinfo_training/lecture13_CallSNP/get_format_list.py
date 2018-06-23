import os
import re
f = os.system("zcat scaffold37_cov106.vcf.gz >scaffold37_cov106.vcf")
f2 = open("scaffold37_cov106.vcf")
#print(f2.read())
my_list = []
content = f2.readlines()
for line in content:
	if re.match('^##(.*)',line):
		continue
	if re.match('^#(.*)',line):
		#print(line)
		#line = line.strip()
		my_list = line.split()
#print(my_list)
 
for i in range(len(my_list)):
	if i >= 9:
		print(my_list[i])
