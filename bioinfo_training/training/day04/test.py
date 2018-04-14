import re
'''
content = 'Hello 1234567 is a number, regex String'
result = re.match('^Hello (\d+).*String$',content)
if result:
    print(result.group(1))
'''

'''
# .*?从少找多
content = 'extra string Hello 1234567 is a number, regex String extra'
result = re.search('Hello.*? (\d+).*?String',content)
if result:
   print(result.group(1))
'''

# r""不允许转义
regex = r"\[P\] (.+?) \[P\]+?"
line = "president [P] Barack Obama [P] met [P] Bill Gates [P] yesterday"
person = re.findall(regex,line)
print(person)

'''
line1 = "by Jeffery Friedl"
result1 = re.match(r"(?=Jeffery)Jeff",line1)

line2 = "see Jeffs books"
result2 = re.match('\b Jeff (?=s\b)', line2)
result3 = re.match('(?<=\b Jeff)(?=s\b)',line2)

print(result3.group(1))'''











