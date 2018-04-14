
f = open('test001.txt', 'r')

letters = []
answer = []

for line in f:
    line.strip("\n")
    letters.append(line)

answer = [letters[3][0],letters[3][1],letters[3][4],letters[3][5],letters[3][6],letters[3][8],letters[3][9]]

print(answer)
f.close()