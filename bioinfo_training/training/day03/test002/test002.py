# total word count for each file
import os
files = os.listdir()
word_count = {}

for file in files:
    if os.path.splitext(file)[1] == ".txt":
        f = open(file)
        info = f.read()
        alist = info.split(' ')  # 将文章按照空格划分开
        word = len(alist)  # 总的单词数
        blankspace = alist.count('')  # 空格的数量
        word_count[file] = word - blankspace



print(word_count)

