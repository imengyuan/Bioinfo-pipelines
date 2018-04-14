
f = open('test001.txt', 'r')

letters = []
answer = []
frequency = {}

for line in f:
    line.strip("\n")
    letters.append(line)

for i in range(10):
    letter = letters[7][i]
    frequency[letter] = letters[7].count(letter)

answer = sorted(frequency.items(),key = lambda item:item[1])
print(answer[0][0])
f.close()