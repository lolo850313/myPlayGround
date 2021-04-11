#函数返回多个值
def get_info():
    name = "alex"
    age = 29
    return name, age

name, age = get_info()
print(name)
print(age)

info = get_info()
print(info)
print(type(info))
