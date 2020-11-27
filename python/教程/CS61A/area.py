#面积公式
def area(r,shape_constant):
    #if r <= 0 ,the terminal will report error
    assert r>0, "A length must be positive"
    return r * r * shape_constant

#正方形面积
def area_square(r):
    return area(r, 1)

#圆形面积
def area_circle(r):
    from math import pi
    return area(r,pi)

print(area_square(3))