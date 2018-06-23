# list distance between two words

f = open('01-The_Philosophers_Stone.txt')
readline = f.readlines()

words = []

for line in readline:
    line = line.replace(',', '')
    line = line.strip()
    wo = line.split(' ')
    words.extend(wo)

while '' in words:
    words.remove('')

word_1 = 'Harry'
word_2 = 'the'


location_1 = words.index(word_1)
location_2 = words.index(word_2)

distance = location_2 - location_1

print(distance)


