def sum_col(list,number):
	thesum=0
	for i in list[1:]:
		thesum+=int(i[number])
	return thesum

filein=open("HKA.01.pl.out","r")
line=filein.readline()
name=line.rstrip().split("\t")
window=1
tempK=[0]*15
tempD=[0]*15
out_list=[]
header=["scaffold","start","end"]
for i in [2,3,5,6,7,8,9,10,11,12,13,14]:
	header.append(name[i]+"D")
	header.append(name[i]+"K")
	header.append(name[i]+"GenomeD")
	header.append(name[i]+"GenomeK")
out_list.append(header)#最终输出文件

line=filein.readline()
while line:
	record=line.rstrip().split("\t")
	if int(record[1])<window*10000:
		for i in [2,3,5,6,7,8,9,10,11,12,13,14]:
			if record[i]=="het":
				tempK[i]+=1 
			if (record[i]=="alt" and record[4]=="ref")or(record[i]=="ref" and record[4]=="alt"):
				tempD[i]+=1
	else:
		start=1+(window-1)*10000
		end=window*10000
		to_add=["scaffold",str(start),str(end)]
		for i in [2,3,5,6,7,8,9,10,11,12,13,14]:
			to_add.append(str(tempD[i]))
			to_add.append(str(tempK[i]))
			to_add.append(str(0))
			to_add.append(str(0))
		out_list.append(to_add)
		window+=1
		tempK=[0]*15
		tempD=[0]*15
		for i in [2,3,5,6,7,8,9,10,11,12,13,14]:
			if record[i]=="het":
				tempK[i]+=1
			if (record[i]=="alt" and record[4]=="ref")or(record[i]=="ref" and record[4]=="alt"):
				tempD[i]+=1
	line=filein.readline()

start=1+(window-1)*10000
end=window*10000
to_add=["scaffold",str(start),str(end)]
for i in [2,3,5,6,7,8,9,10,11,12,13,14]:
	to_add.append(str(tempD[i]))
	to_add.append(str(tempK[i]))
	to_add.append(str(0))
	to_add.append(str(0))
out_list.append(to_add)
		
filein.close()

for i in [5,6,9,10,13,14,17,18,21,22,25,26,29,30,33,34,37,38,41,42,45,46,49,50]:
	temp_sum=sum_col(out_list,i-2)
	for j in out_list[1:]:
		j[i]=str(temp_sum)

fileout=open("04.result.txt","w")
for i in out_list:
	print("\t".join(i),file=fileout)
fileout.close()


