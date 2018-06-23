# each character counts

f = open('01-The_Philosophers_Stone.txt')
content = f.read()

letter_count = {}

letters = [chr(i) for i in range(97,123)]
upper = [chr(j) for j in range(65,91)]
letters.extend(upper)

for letter in letters:
    letter_count[letter] = content.count(letter)


print(letter_count)






