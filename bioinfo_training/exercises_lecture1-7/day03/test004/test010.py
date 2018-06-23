
f = open('test001.txt', 'r')

letters = []
answer = []
difference = {}

for line in f:
    line.strip("\n")
    letters.append(line)


for i in range(1, 10):
    letter = letters[8][i]
    difference[letter] = ord(letter)-ord(letters[8][0])
    if difference[letter] == 1:
        answer.append(letter)

if answer == []:
    print("no such letters")
else :
    print(answer)
f.close()