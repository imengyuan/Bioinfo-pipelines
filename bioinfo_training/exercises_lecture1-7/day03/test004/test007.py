
f = open('test001.txt', 'r')

letters = []
answer = []

for line in f:
    line.strip("\n")
    letters.append(line)

answer = [letters[5][3],letters[5][4],letters[5][6],letters[5][7],letters[5][8]]

print(answer)
f.close()