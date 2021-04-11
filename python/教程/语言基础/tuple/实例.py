#创建元组
tup11 = ()
tup12 = (50,)

#访问元组
tup2 = (1, 2, 3, 4)
print(tup2[0])
print(tup2[1:3])

#元组不能被修改，只能被拼接
tup31 = (12, 34.56)
tup32 = ('abc', 'xyz')
print(tup31 + tup32)

#除了不能被修改以外都跟list类似
print(len(tup32))