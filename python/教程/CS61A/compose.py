def square(x):
    return x * x 
def make_adder(n): 
    def adder(k): 
        return k + n 
    return adder 

def compose(f, g): 
    def h(x): 
        return f(g(x)) 
    return h 

print(compose(square, make_adder(2)))
print(make_adder(2))
print(compose(square, make_adder(2))(3))