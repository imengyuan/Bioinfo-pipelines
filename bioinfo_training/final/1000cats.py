# 生成一个含有1000只形状有差异的猫的svg文件
# http://222.18.10.115/class/2018-Spring/003-SVG.html

# 20行x每行50个=1000个

import random

f = open("1000cats.svg", "w")

cx1 = [0] * 50
cy1 = [0] * 20
cx2 = [0] * 50
cy2 = [0] * 20
cx3 = [0] * 50
cy3 = [0] * 20
cx4 = [0] * 50
cy4 = [0] * 20
cx5 = [0] * 50
cy5 = [0] * 20
cx6 = [0] * 50
cy6 = [0] * 20
cx7 = [0] * 50
cy7 = [0] * 20
cx8 = [0] * 50
cy8 = [0] * 20
cx9 = [0] * 50
cy9 = [0] * 20
cx10 = [0] * 50
cy10 = [0] * 20
cx11 = [0] * 50
cy11 = [0] * 20
cx12 = [0] * 50
cy12 = [0] * 20
cx13 = [0] * 50
cy13 = [0] * 20
cx14 = [0] * 50
cy14 = [0] * 20
cx15 = [0] * 50
cy15 = [0] * 20
cx16 = [0] * 50
cy16 = [0] * 20
cx17 = [0] * 50
cy17 = [0] * 20
cx18 = [0] * 50
cy18 = [0] * 20
cx19 = [0] * 50
cy19 = [0] * 20
cx20 = [0] * 50
cy20 = [0] * 20
cx21 = [0] * 50
cy21 = [0] * 20

# write svg headlines
svg_head ="""<?xml version="1.0"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="10000" height="10000" xmlns="http://www.w3.org/2000/svg">
<title>Cat</title>
<desc>Stick Figure of a Cat</desc>
<!-- the drawing will go here -->
"""
f.write(svg_head)


for x in range(50):
    for y in range(20):
        r1 = 160
        r2 = 200
        cx1[x] = str(220 + x * r1)
        cy1[y] = str(120 + y * r2)
        cx2[x] = str(200 + x * r1)
        cy2[y] = str(80 + y * r2)
        cx3[x] = str(240 + x * r1)
        cy3[y] = str(80 + y * r2)
        cx4[x] = str(220 + x * r1)
        cy4[y] = str(110 + y * r2)
        cx5[x] = str(208 + x * r1)
        cy5[y] = str(88 + y * r2)
        cx6[x] = str(210 + x * r1)
        cy6[y] = str(110 + y * r2)
        cx7[x] = str(230 + x * r1)
        cy7[y] = str(110 + y * r2)
        cx8[x] = str(157 + x * r1)
        cy8[y] = str(69 + y * r2)
        cx9[x] = str(180 + x * r1)
        cy9[y] = str(y * r2)
        cx10[x] = str(180 + x * r1)
        cy10[y] = str(y * r2)
        cx11[x] = str(220 + x * r1)
        cy11[y] = str(40 + y * r2)
        cx12[x] = str(220 + x * r1)
        cy12[y] = str(40 + y * r2)
        cx13[x] = str(260 + x * r1)
        cy13[y] = str(y * r2)
        cx14[x] = str(260 + x * r1)
        cy14[y] = str(y * r2)
        cx15[x] = str(283 + x * r1)
        cy15[y] = str(69 + y * r2)
        cx16[x] = str(180 + x * r1)
        cy16[y] = str(150 + y * r2)
        cx17[x] = str(190 + x * r1)
        cy17[y] = str(160 + y * r2)
        cx18[x] = str(190 + x * r1)
        cy18[y] = str(160 + y * r2)
        cx19[x] = str(250 + x * r1)
        cy19[y] = str(160 + y * r2)
        cx20[x] = str(250 + x * r1)
        cy20[y] = str(160 + y * r2)
        cx21[x] = str(260 + x * r1)
        cy21[y] = str(150 + y * r2)
        col1 = str(random.randint(1, 255))
        col2 = str(random.randint(1, 255))
        col3 = str(random.randint(1, 255))

        f.writelines('<circle cx="'+cx1[x]+'" cy="'+cy1[y]+'" r="80" style="stroke:black;fill:white;"/>''\r'
                 '<circle cx="'+cx2[x]+'" cy="'+cy2[y]+'" r="10" style="stroke:black;fill:rgb('+col1+','+col2+','+col3+');"/>''\r'
                 '<circle cx="'+cx3[x]+'" cy="'+cy3[y]+'" r="10" style="stroke:black;fill:rgb('+col1+','+col2+','+col3+');"/>''\r'
                 '<ellipse cx="'+cx4[x]+'" cy="'+cy4[y]+'" rx="10" ry="20"  style="stroke:black;fill:pink;"/>''\r'
                 '<rect x="'+cx5[x]+'" y="'+cy5[y]+'" width="25" height="22" style="stroke:none;fill:white;"/>''\r'
                 '<line x1="'+cx6[x]+'" y1="'+cy6[y]+'" x2="'+cx7[x]+'" y2="'+cy7[y]+'" style="stroke:black;"/>''\r'
                 '<line x1="'+cx8[x]+'" y1="'+cy8[y]+'" x2="'+cx9[x]+'" y2="'+cy9[y]+'" style="stroke:black;"/>''\r'
                 '<line x1="'+cx10[x]+'" y1="'+cy10[y]+'" x2="'+cx11[x]+'" y2="'+cy11[y]+'" style="stroke:black;"/>''\r'
                 '<line x1="'+cx12[x]+'" y1="'+cy12[y]+'" x2="'+cx13[x]+'" y2="'+cy13[y]+'" style="stroke:black;"/>''\r'
                 '<line x1="'+cx14[x]+'" y1="'+cy14[y]+'" x2="'+cx15[x]+'" y2="'+cy15[y]+'" style="stroke:black;"/>''\r'
                 '<line x1="'+cx16[x]+'" y1="'+cy16[y]+'" x2="'+cx17[x]+'" y2="'+cy17[y]+'" style="stroke:black;"/>''\r'
                 '<line x1="'+cx18[x]+'" y1="'+cy18[y]+'" x2="'+cx19[x]+'" y2="'+cy19[y]+'" style="stroke:black;"/>''\r'
                 '<line x1="'+cx20[x]+'" y1="'+cy20[y]+'" x2="'+cx21[x]+'" y2="'+cy21[y]+'" style="stroke:black;"/>''\r')


f.write('</svg>')
f.close()
