# 生成ABCD组成的全部十位字符串
from itertools import product

src_list = ['A','B','C','D']
product = list(product(src_list, repeat=10))
string_list = []

f = open('test001.txt','w')
for term in product:
    p = "".join(list(term))
    string_list.append(p)
    f.write(p)

print(string_list)


