import re
while True:
    email = input('Enter email like abc@cde.com :')
    if email == 'stop': break

    result = re.match('(.+)@(.+)', email)
    print("first is ",result.group(1))
    print("last is ", result.group(2))
