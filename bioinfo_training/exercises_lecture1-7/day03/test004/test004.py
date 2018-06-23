
f = open('test001.txt', 'r')

letters = []
answer = []

for line in f:
    line.strip("\n")
    letters.append(line)

answer = [letters[2][2],letters[2][5],letters[2][1],letters[2][3]]

print(answer)
f.close()