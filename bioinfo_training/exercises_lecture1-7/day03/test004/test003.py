
f = open('test001.txt', 'r')

letters = []

for line in f:
    line.strip("\n")
    letters.append(line)

answer = letters[1][4]

print(answer)
f.close()