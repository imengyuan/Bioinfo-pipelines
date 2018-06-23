
f = open('test001.txt', 'r')

letters = []
answer = []

for line in f:
    line.strip("\n")
    letters.append(line)

answer = [letters[4][0],letters[4][1],letters[4][4],letters[4][5],letters[4][6],letters[4][8],letters[4][9]]

print(answer)
f.close()