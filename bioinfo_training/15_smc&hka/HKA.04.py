import re
D,K = 0, 0
wind = []
scaffold =''
pos = ''
first_line=[]
names=[2,3,5,6,7,8,9,10,11,12,13]
for name in names:
	first_line.append(names[i]+"D")
	first_line.append(names[i]+"K")
	first_line.append(names[i]+"GenomeD")
	first_line.append(names[i]+"GenomeK")
f = open("HKA.01.pl.out")
lines = f.readlines()
i = 0

for n in names:
	for line in lines:
		if re.match('^#',line):
			continue
		a = line.split()
		scaffold = a[0]
		pos = a[1]
		wind = int(pos/10000)+1
		if(a[n[i]] == 'het'):
			K+=1
			wind[wind[K]]+=1
		elif:
			if a[n[i]]=='ref' and a[4]=='alt' :
				D+=1
				wind[wind[D]]+=1
			elif a[n[i]]=='alt' and a[4]=='ref':
				D+=1
				wind[wind[D]]+=1
	name_line.ap
	print("#scaffold\tD\tK\tGenomeD\tGenomeK\n")				


