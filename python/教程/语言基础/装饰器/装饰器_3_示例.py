# 将函数作为参数传给另一个函数
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("before executing a_func()")
        a_func()
        print("after executing a_func()")
    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()

#增加装饰器
@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()