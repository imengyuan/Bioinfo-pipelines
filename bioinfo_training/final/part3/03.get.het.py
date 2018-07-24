#从vcf文件中得到每个个体的ref/alt数除以 no-miss数
import os
import re
f = os.system("zcat scaffold4.vcf.gz >scaffold4.vcf")
f2 = open("scaffold4.vcf")

content = f2.readlines()
for line in content:
    total_list = []
    if re.match('^#(.*)',line):
        continue
    else:
        my_list = []
        het_list = []

        my_list = line.split()
        het_list.append(my_list[0])
        het_list.append(my_list[1])
        het,ref,alt,mis = 0,0,0,0
        for i in range(len(my_list)):
            if re.match('0\/1',my_list[i]):
                het+=1
            if re.match('1\/1',my_list[i]):
                alt+=1
            if re.match('0\/0',my_list[i]):
                ref+=1
            if re.match('\.\/\.',my_list[i]):
                mis+=1
        if het+ref+alt != 0:
            het_value = het/float(het+ref+alt)
        het_list.append([het_value])
    print(het_list)










