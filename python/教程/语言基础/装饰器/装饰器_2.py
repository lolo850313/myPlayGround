# 将函数作为参数传给另一个函数
def hi():
    print("say hi")

def say(func):
    print("if i meet somebody")
    func()

say(hi)
