# list distance between 2 words

import os
files = os.listdir()
word_distance = {}

word_1 = 'Harry'
word_2 = 'the'

for file in files:
    if os.path.splitext(file)[1] == ".txt":

        f = open(file)
        readline = f.readlines()
        words = []
        for line in readline:
            line = line.replace(',', '')
            line = line.strip()
            wo = line.split(' ')
            words.extend(wo)

        while '' in words:
            words.remove('')


        location_1 = words.index(word_1)
        location_2 = words.index(word_2)

        distance = location_2 - location_1
        word_distance[file] = distance

print(word_distance)