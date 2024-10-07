# def double(x):
#     return x*2

def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3



print(double(20))
print(cube(9))
print(avg(10, 20, 30))
print(appl(cube, 2))