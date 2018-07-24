
f=open("test001.out","w")

for i in range(0,1000):
    x=pow((2015141494141+i),3)
    f.write(str(x))
    f.write("\n")

f.close()


