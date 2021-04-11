from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_strings = func.__name__ + " was called"
            print(log_strings)

            with open(self.logfile, "a") as opened_file:
                opened_file.write(log_strings + "\n")

            self.notify()

            return func(*args, *kwargs)

        return wrapped_function()

    def notify(self):
        pass

@logit()
def myfunc1():
    pass