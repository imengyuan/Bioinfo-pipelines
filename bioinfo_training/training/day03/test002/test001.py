# total line number in each txt
import os
files = os.listdir()
line_number = {}


for file in files:
    if os.path.splitext(file)[1] == ".txt":
        line_number[file] = len(open(file,'rU').readlines())

print(line_number)