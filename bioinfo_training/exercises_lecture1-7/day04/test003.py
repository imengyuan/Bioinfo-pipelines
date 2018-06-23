# 各种正则表达式
import re

# 1-13查找
# 查找所有汉字
chinese = "哈我在hhh上课hhh"
r_chinese = u"[\u4e00-\u9fa5]+"

# email
email = "viciayuan@hotmail.com"
r_email = "[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-zA-Z]+"

# url
url = r"https://en.wikipedia.org/wiki/url"
r_url = "[a-zA-Z]+:\/\/[a-zA-Z0-9\.\_]+\/[a-zA-Z0-9\_\/]*"

# 4 phone number
phone = r"028-85402398"
r_phone = "\d{3}\-\d{3,8}"

# 5. qq
qq = "1346662511"
r_qq = "[1-9]\d{5,15}"

# 6. ID number
id = "12345678901234567X"
r_id = "[1-9]\d{16}[0-9xX]"

# 7. postcode
postcode = "611025"
r_postcode = "\d{6}"

# 8. chinese id
id = "12345678901234567X"
r_id = "[1-9]\d{16}[0-9xX]"


letter = "hjkdJJK1223l"
# 9. letter
r_leter = "[a-zA-Z]+"
# 10. upper
r_upper = "[A-Z]+"
# 11. lower
r_lower = "[a-z]+"
# 12
r_12 = "[0-9a-zA-Z]+"
# 13
r_13 = "[0-9a-zA-Z\_]+"


'''
result = re.findall(r_23, "9ab")
if result:
    print(result)
else:
    print("error")'''


# 14-38验证输入
number = r"0902138"
# 14
r_14 = "^[0-9]*$"
# 15
r_15 = "^[0-9]{4}"
# 16
r_16 = "^[0-9]{0,4}"
# 17
r_17 = "^[0-9]{1,4}"
# 18
r_18 = "^[0-9]*"
# 19
r_19 = "^[0-9]*\.[0-9]{2}$"
# 20
r_20 = "^[0-9]*\.[0-9]{1,3}$"
# 21
r_21 = "^[1-9][0-9]*$"
# 22
r_22 = "^\-[1-9][0-9]*$"
# 23
r_23 = ".{3}"
# 24-28对应9-13

# 29
r_29= "^[a-zA-z]+.{5,17}"
# 30
r_30 = "[0-9\_a-zA-Z]*"
# 31
r_31 = "[\^\%\&\,\;\=\?\$]+"
# 32-36对应前面的答案

# 37
r_37 = "[1-9]|1[0-2]"
# 38
r_38 = "[1-9]|1[0-9]|2[0-9]|3[0-1]"

# 更改正则表达式规则验证输入，这里默认测试r_14
while True:
    line = input('please input the string :')
    if line == 'stop': break

    result = re.match(r_14, line)
    if result:
        print(result.group(0))
    else:
        print("error")





