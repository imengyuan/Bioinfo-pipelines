import re

f = open('email.txt')
readline = f.readlines()

r_0 = "^From: (.+) \(([\w\s]+)\)"
r_1 = "^Reply\-To: (.+)$"
r_2 = "^To: (.+)$"
r_3 = "^Subject(.+)"
r_4 = "^From elvis (.+)$"

for line in readline:
    result_0 = re.match(r_0, line)
    result_1 = re.match(r_1, line)
    result_2 = re.match(r_2, line)
    result_3 = re.match(r_3, line)
    result_4 = re.match(r_4, line)

    if result_0:
        name = result_0.group(2)
    if result_1:
        line_1 = result_1.group(1)
    if result_2:
        line_2 = result_2.group(1)
    if result_3:
        line_3 = result_3.group(1)
    if result_4:
        line_4 = result_4.group(1)



print("To: "+line_1+name)
print("from: "+line_2)
print("Subject: Re"+line_3)
print("On " +line_4+" "+name+" wrote:\n")

for line in readline[-4:]:
    print(line.strip())
