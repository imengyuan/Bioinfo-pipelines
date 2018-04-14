
while True:
    a = input('Enter string a:')
    if a == 'stop': break
    b = input('Enter string b:')
    if b == 'stop': break

    l = [a,b]
    l.sort()

    print(l[0],',zz',l[1])
