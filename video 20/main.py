def calculateSum(a,b):
    Sum = (a + b)
    print(Sum)

def isGreater(a, b):
    if(a < b):
        print("First number is greater than second")
    elif(a == b):
        print("Both numbers are equal")
    else:
        print("Second number is greater than first")

def isLesser(a , b):
    pass

a = 5
b = 8
isGreater(a, b)
calculateSum(a, b)

c = 88
d = 74
isGreater(c, d)
calculateSum(c, d)

e = 10
f = 10
isGreater(e, f)
calculateSum(e, f)

def name(fname, lname):
    print("Hello,", fname, lname)
name("Aditya", "Sura")