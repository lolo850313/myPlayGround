def rotate_letter(letter, n):
    #ord()是chr()或unichr()的配对函数，超过python的定义范围引发一个typeerror 
    #ord('a') = 97 ord('b')=98
    if letter.isupper():
        start = ord("A")
    elif letter.islower():
        start = ord("a")
    #非大小写字母时，不需要轮转
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word,n):
    res = ""
    for letter in word:
        res += rotate_letter(letter,n)
    return res

if __name__ =="__main__":
    print(rotate_word("cheer", 7))
    print(rotate_word("melon", -10))
    print(rotate_word("sleep", 9))


