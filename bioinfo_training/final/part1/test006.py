import re


from itertools import product

src_list = ['A','G','C','T']
product = list(product(src_list, repeat=3))
string_list = []


for term in product:
    p = "".join(list(term))
    string_list.append(p)
#print(string_list)

f1 = open("genome.fasta","r")
f2 = open("test006.out","w")
lines = f1.readlines()
for line in lines:
    if line[0]=="^":
        continue
    final = []
    frq = []
    for i in range(len(string_list)):
        frq[i]=line.count(string_list[i])
        final.append([string_list[i],frq[i]])

    f2.write(final)

f1.close()
f2.close()