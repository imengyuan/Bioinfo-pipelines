
f1=open("test003.out","r")
f2=open("test004.out","w")
list = []
lines=f1.readlines()
for line in lines:
    line=line.strip()
    list.append(int(line))
    
list.sort()
for item in list:
    f2.write(str(item))
    f2.write("\n")
f1.close()
f2.close()

