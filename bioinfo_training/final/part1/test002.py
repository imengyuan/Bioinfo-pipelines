
f=open("test002.out","w")

for i in range(0,1000):
    x=pow((2015141494141+i),3)
    answer=list(str(x))
    #print(answer[1])
    f.write(str(answer[1]))
    f.write("\n")

f.close()



