
f = open('test001.txt', 'r')

letters = []
answer = []
frequency = {}

for line in f:
    line.strip("\n")
    letters.append(line)

for i in range(10):
    letter = letters[9][i]
    frequency[letter] = letters[9].count(letter)

answer = sorted(frequency.items(),key = lambda item:item[1])

print(answer[-1][1] - answer[0][1])
f.close()