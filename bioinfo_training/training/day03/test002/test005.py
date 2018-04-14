# how many empty lines

import os
files = os.listdir()
empty_line = {}

for file in files:
    if os.path.splitext(file)[1] == ".txt":
        f = open(file)
        readline = f.readlines()
        emptyline = 0
        for line in readline:
            line = line.strip()
            if line == '':
                emptyline += 1

        empty_line[file] = emptyline

print(empty_line)