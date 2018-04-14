# each character file

import os
files = os.listdir()
letter_numbers = {}
letter_count = {}

letters = [chr(i) for i in range(97, 123)]
upper = [chr(j) for j in range(65, 91)]
letters.extend(upper)

for file in files:
    if os.path.splitext(file)[1] == ".txt":
        f = open(file)
        content = f.read()

        for letter in letters:
            letter_count[letter] = content.count(letter)
    letter_numbers[file] = letter_count


print(letter_numbers)