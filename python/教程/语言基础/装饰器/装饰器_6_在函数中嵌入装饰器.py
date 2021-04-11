from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            with open(logfile, "a") as opened_file:
                opened_file.write(log_string + "\n")
            return func(*args, **kwargs)
        return with_logging
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串