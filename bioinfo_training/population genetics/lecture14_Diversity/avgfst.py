import sys

filein=open(sys.argv[1],"r")
filein.readline()
line=filein.readline()
sum=0
number=0
while line:
	record=line.rstrip().split("\t")
	value=record[2]
	if value!="-nan":
		sum+=float(value)
		number+=1
	line=filein.readline()
print(sum/number)
filein.close()
