# 一个类实例要变成一个可调用对象
# 凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象
# 判断对象是否为可调用对象可以用函数 callable

class Clanguage:
    def __call__(self, name, add):
        print("调用__call__方法", name, add)

clangs = Clanguage()
clangs("c语言", "http")
clangs.__call__("c语言", "http")

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print("my name " + self.name)
        print("my friend " + friend)

p = Person("tom", "male")
p("tony")
#callable() 函数用于检查一个对象是否是可调用的。
print(callable(p))