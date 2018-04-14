import re
while True:
    email = input('Enter email like aB1@cde.com :')
    if email == 'stop': break

    result = re.match('([a-z]+[A-Z]+[0-9]+)|([a-z]+[0-9]+[A-Z]+)|([0-9]+[a-z]+[A-Z]+)|([0-9]+[A-Z]+[a-z]+)|([A-Z]+[0-9]+[a-z]+)|([A-Z]+[a-z]+[0-9]+)@(.+)\.com', email)

    if result:
        print("ok")
    else:
        print("error")
