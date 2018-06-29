'''
把mdist转换为phylip
'''
count=0
file_mdist=open("plink.mdist","r")
file_id=open("plink.mdist.id","r")
file_out=open("plink.mdist.phylip","w")
out_record=[]
line1=file_mdist.readline()
line2=file_id.readline()
while line1 and line2:
	line1=line1.rstrip()
	line2=line2.rstrip()
	name=line2.split("\t")[0]
	name=name+" "*(10-len(name))
	string="\t".join([name,line1])
	out_record.append(string)
	count+=1
	line1=file_mdist.readline()
	line2=file_id.readline()
print(" \t",count,file=file_out)
for i in out_record:
	print(i,file=file_out)
file_mdist.close()
file_id.close()
file_out.close()
