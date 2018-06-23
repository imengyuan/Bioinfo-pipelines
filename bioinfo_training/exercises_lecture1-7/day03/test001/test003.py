# each word freguency


def read_file():
    f = open('01-The_Philosophers_Stone.txt')
    readline = f.readlines()

    word = []

    for line in readline:
        line = line.replace(',', '')
        line = line.strip()
        wo = line.split(' ')
        word.extend(wo)

    return word


def clear_account(lists):
    wordkey = {}
    wordkey = wordkey.fromkeys(lists)

    word_1 = list(wordkey.keys())

    for i in word_1:
        wordkey[i] = lists.count(i)
    return wordkey


def wordsort(wordkey):
    # 删除''字符
    del [wordkey['']]

    wordkey_sorted = sorted(wordkey.items(), key=lambda d: d[1], reverse=True)

    wordkey_sorted = dict(wordkey_sorted)
    return wordkey_sorted

def main(wordkey_sorted):
    print(wordkey_sorted)

main(wordsort(clear_account(read_file())))

