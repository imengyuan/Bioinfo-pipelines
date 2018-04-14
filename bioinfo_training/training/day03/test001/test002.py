 # total word count


f = open('01-The_Philosophers_Stone.txt')
info = f.read()

alist = info.split(' ')  # 将文章按照空格划分开

word = len(alist)  # 总的单词数
blankspace = alist.count('')  # 空格的数量
print("total word count is ", word - blankspace)

f.close()


