# 生成所有选项可能的组合
from itertools import product

src_list = ['A', 'B', 'C', 'D']
product = list(product(src_list, repeat=10))
string_list = []
for term in product:
    p = "".join(list(term))
    string_list.append(p)



# print(string_list)


# 数组t为每题所选选项
def question_1(t):
    if t[0] == 'A':
        return 'A'
    elif t[0] == 'B':
        return 'B'
    elif t[0] == 'C':
        return 'C'
    elif t[0] == 'D':
        return 'D'


def question_2(t):
    if t[4] == 'C':
        return 'A'
    elif t[4] == 'D':
        return 'B'
    elif t[4] == 'A':
        return 'C'
    elif t[4] == 'B':
        return 'D'


def question_3(t):
    if t[6 - 1] == t[2 - 1] == t[4 - 1] != t[3 - 1]:
        return 'A'
    elif t[2 - 1] == t[4 - 1] == t[3 - 1] != t[6 - 1]:
        return 'B'
    elif t[4 - 1] == t[3 - 1] != t[6 - 1] != t[2 - 1]:
        return 'C'
    elif t[3 - 1] != t[6 - 1] != t[2 - 1] != t[4 - 1]:
        return 'D'


def question_4(t):
    if t[1 - 1] == t[5 - 1]:
        return 'A'
    elif t[2 - 1] == t[7 - 1]:
        return 'B'
    elif t[1 - 1] == t[9 - 1]:
        return 'C'
    elif t[6 - 1] == t[10 - 1]:
        return 'D'


def question_5(t):
    if t[4] == t[8 - 1]:
        return 'A'
    elif t[4] == t[4 - 1]:
        return 'B'
    elif t[4] == t[9 - 1]:
        return 'C'
    elif t[4] == t[7 - 1]:
        return 'D'


def question_6(t):
    if t[7] == t[2 - 1] == t[4 - 1]:
        return 'A'
    elif t[7] == t[1 - 1] == t[6 - 1]:
        return 'B'
    elif t[7] == t[3 - 1] == t[10 - 1]:
        return 'C'
    elif t[7] == t[5 - 1] == t[9 - 1]:
        return 'D'


def question_7(t):
    min = 10

    choices = ['A', 'B', 'C', 'D']
    for i in choices:
        if t.count(i) <= min:
            min = t.count(i)
            choice = i
    if choice == 'C':
        return 'A'
    elif choice == 'B':
        return 'B'
    elif choice == 'A':
        return 'C'
    elif choice == 'D':
        return 'D'


def question_8(t):
    for i in [7, 5, 2, 10]:
        if abs(ord(t[i - 1]) - ord(t[0])) == 1:
            return True


def question_9(t):
    x = 0
    if t[0] == t[5]:
        for i in range(11):
            if t[i - 1] != t[4]:
                x = i
    elif t[0] != t[5]:
        for i in range(11):
            if t[i - 1] == t[4]:
                x = i

    if x == 6:
        return 'A'
    elif x == 10:
        return 'B'
    elif x == 2:
        return 'C'
    elif x == 9:
        return 'D'


def question_10(t):
    frequency = {}
    answer = []
    for i in ['A', 'B', 'C', 'D']:
        frequency[i] = t.count(i)
    answer = sorted(frequency.items(), key=lambda item: item[1])
    x = answer[-1][1] - answer[0][1]
    
    if x == 3:
        return 'A'
    elif x == 2:
        return 'B'
    elif x == 4:
        return 'C'
    elif x == 1:
        return 'D'




answer = ''
for choice in string_list:
    #print("question_10")
    if question_10(choice) == choice[10 - 1]:
        #print("question_9")
        if question_9(choice) == choice[9 - 1]:
            #print("question_8")
            if question_8(choice):
                #print("question_7")
                if question_7(choice) == choice[7 - 1]:
                    #print("question_6")
                    if question_6(choice) == choice[6 - 1]:
                        #print("question_5")
                        if question_5(choice) == choice[5 - 1]:
                            #print("question_4")
                            if question_4(choice) == choice[4 - 1]:
                                #print("question_3")
                                if question_3(choice) == choice[3 - 1]:
                                    #print("question_2")
                                    if question_2(choice) == choice[2 - 1]:
                                        #print("question_1")
                                        if question_1(choice) == choice[1 - 1]:
                                            answer = choice
                                            print("the right answer is ", answer)
