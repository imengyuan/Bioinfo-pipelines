
f = open('test001.txt', 'r')

letters = []
answer = []

for line in f:
    line.strip("\n")
    letters.append(line)

answer = [letters[6][0],letters[6][1],letters[6][2],letters[6][3],letters[6][4],letters[6][5],letters[6][7],letters[6][8]]

print(answer)
f.close()