#优点：由于是不可变的， 所以可以作为dict的key和放进set中
#存储空间更小，创建更快，多并发不需要加锁，不用担心安全问题

#当元组中只有一个元素时，最后必须要有逗号，否则会被认为是其他类型
temp = (1,)
print(type(temp))

temp = (1)
print(type(temp))

temp = ("1")
print(type(temp))

print(8 * (8))
print(8 * (8,))