
import random
f=open("test003.out","w")

for i in range(0,1000):
    x=int(random.random()*100)
    f.write(str(x))
    f.write("\n")
    
f.close()


