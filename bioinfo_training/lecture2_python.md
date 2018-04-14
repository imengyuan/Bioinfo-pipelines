# python3 语言基础与实践

[课件地址](http://222.18.10.115/class/2018-Spring/002-Python.html)

感觉这随意的笔记感觉只能自己看懂了

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
repete: s*5
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
```
# day03/test001 读取01-The_Philosophers_Stone.txt，输出下列结果
total line numbers
total word count
each word freguency
each character counts
how many empty lines
list distance between two words

# day03/test002 读取 *.txt
对每个txt文件输出上面各结果

# day03/test004 生成ABCD组成的全部字符串，并进行下列的取值和计算
取第i行第j，k,l个字符
取第i行出现频率最少、与第1位ascii差异位1的字符
第i行出现次数最多与最少之差
```

* 判断与循环...
要用到上一问生成的字符串去判断
![](questions.png)


