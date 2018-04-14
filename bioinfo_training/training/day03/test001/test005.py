# how many empty lines

f = open('01-The_Philosophers_Stone.txt')
readline = f.readlines()

empty_line = 0
for line in readline:
    line = line.strip()
    if line == '':
        empty_line +=1

print("numbers of empty lines is ", empty_line)
