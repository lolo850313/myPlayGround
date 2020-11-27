#判断字符串中是否有三个连续重复两次字母
def is_tripple_word(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1
            count = 0
    return False

def find_triple_word():
    fin = open("d:\\lolo\\python\\教程\\think python\\words.txt")
    for line in fin:
        word = line.strip()
        if is_tripple_word(word):
            print(word)

find_triple_word()