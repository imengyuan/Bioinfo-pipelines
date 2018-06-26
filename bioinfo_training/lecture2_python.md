# python3 语言基础与实践


## 一些基础
* object type
```
list (range(10)) 0,,9
dictionary {key: value}
tuple ()
set('abd') {'a','b','c'}
```

* operator
```
if else
and, or
is is not, in not in
x/y (true), x//y (floor)
x[i]  index
```

* Strings
```
splice: s[-1], s[1:3]
concatenate: s+'abc'
repeat: s*5
string to list: l = list('abcd')
join by empty: ''.join(l)
find offset: s.find('pa')
replace: s.replace('abc','de')
s.split(',')
s.upper
s.rstrip() remove right whitespaces
%,  .format() #day02/test005.txt
ord('a') # ascii
```

* List
```
len(l) #number of the items in list
[: ], +, * #like string
l.sort()
l.reverse()
2 dimension list [[1,2],[1,2]]
```

* Tuple
like a list but can't be changed

* Dictionaries
```
d = dict(zip(['x','y','z'],[1,2,3]))
nested dictionaries
ks = list(d.keys())
```

* read file, write file
* docstrings
* shell commands
```
import os
f = os.open('dir')
f.readline()
f.read(50)

os.getcwd()
os.chdir()
os.system()
os.popen()
import glob
glob.glob("*") #列举当前目录下所有文件

```

<br>

## Exercises

* 读取键盘输入
```
while True:
    a = input('Enter a:')
    if a == 'stop': break
    b = input('Enter b:')
    if b == 'stop': break

    print("a + b = ", int(a)+int(b))
```

* 文件读写，字符串处理
```python
# day03/test001 读取01-The_Philosophers_Stone.txt，输出下列结果
#test001 total line numbers
count = len(open('01-The_Philosophers_Stone.txt','rU').readlines())
#test002 total word count
f = open('01-The_Philosophers_Stone.txt')
info = f.read()
alist = info.split(' ')  # 将文章按照空格划分开
word = len(alist)  # 总的单词数
blankspace = alist.count('')  # 空格的数量
print("total word count is ", word - blankspace)
f.close()
#test003 each word freguency

# test004 each character counts
# test005 how many empty lines
# test006 list distance between two words

# day03/test002 读取 *.txt 对每个txt文件输出上面各结果
```


生成ABCD组成的全部字符串，并进行下列的取值和计算
```python
# day03/test004 
#test001 生成ABCD组成的全部字符串
#取第i行第j，k,l个字符
#取第i行出现频率最少、与第1位ascii差异位1的字符
#第i行出现次数最多与最少之差
```
输出 test001.txt
```
AAAAAAAAAA
AAAAAAAAAB
AAAAAAAAAC
AAAAAAAAAD
AAAAAAAABA
AAAAAAAABB
AAAAAAAABC
AAAAAAAABD
```

* 判断与循环...
要用到上一问生成的字符串去判断
![](questions.png)


