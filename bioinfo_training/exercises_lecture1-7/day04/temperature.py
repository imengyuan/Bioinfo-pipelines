import re

t = input('Enter a temperature value (eg. 32F, 100C, etc.): ')


result = re.match('([\+\-]?[0-9]+)([CF])', t)

#print(result.group(2))

if result:
    num = int(result.group(1))
    type = result.group(2)

    if type == 'C':
        c = num
        f = (c * 9 / 5) + 32
    else:
        f = num
        c = (f - 32) * 5 / 9

    print("%.2f C is %.2f F" % (c,f))
else:
    print("wrong input type!")
