import os
import re
f = os.system("zcatscaffold4.vcf.gz >scaffold4.vcf")
f2 = open("scaffold4.vcf")

content = f2.readlines()
for line in content:
	total_list = []
	if re.match('^#(.*)',line):
		continue
	else:
		my_list = []
		freq_list = []
		#print(line)
		#line = line.strip()
		my_list = line.split()
		freq_list.append(my_list[0])
		freq_list.append(my_list[1])
		#freq_list.append(2)
		#calculate N_CHR
		cnt = 0
		for i in range(len(my_list)):
			if re.match('0\/0',my_list[i]) or re.match('0\/1',my_list[i]) or re.match('1\/1',my_list[i]):
				cnt += 1
				
		#freq_list.append(cnt*2)
		#calculate {ALLELE:FREQ}
		a = my_list[3]# ref
		b = my_list[4]# alt
		cnt_a,cnt_b = 0,0
		freq_a,freq_b = 0,0
		for i in range(len(my_list)):
			if re.match('0\/1',my_list[i]):
				cnt_a += 1
				cnt_b += 1
			if re.match('1\/1',my_list[i]):
				cnt_b += 2
			if re.match('0\/0',my_list[i]):
				cnt_a += 2
		if cnt_a+cnt_b != 0:
			freq_a = cnt_a / float(cnt_a+cnt_b)
			freq_b = 1- freq_a
		term_4 = str(a)+":"+str(freq_a)+" "+str(b)+":"+str(freq_b)
		if cnt*2*(cnt*2-1) != 0:
		    pi = cnt_a * cnt_b*2/float(cnt*2*(cnt*2-1))
		#print(cnt*2,a,cnt_a,b,cnt_b)
		#freq_list.append(term_4)
		freq_list.append(pi)	
	print(freq_list)










