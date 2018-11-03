
f = open("02.HKA.out")
lines = f.readlines()
header_names = ["scaffold","start","end"]
scaffold = ''
out_list = []
tmpK

pos = ''
wind = ''
for line in lines:
	if re.match('^#',line):
		name = line.rstrip().split("\t")
		names =name[1:] - 'Pdel' 
		for name in names:
			header_names.append(name+"D")
			header_names.append(name+"K")
			header_names.append(name+"GenomeD")
			header_names.append(name+"GenomeK")
	else:
		a = line.rstrip().split("\t")
		pos = a[1]
		

		for n in [2,3,5,6,7,8,9,10,11,12,13,14]:
			if a[n] == "het":
				K += 1
				  		
				if (record[i]=="alt" and record[4]=="ref")or(record[i]=="ref" and record[4]=="alt"):
    			D += 1
				
			out_list.append[K,D,]






#
i = 0
				


