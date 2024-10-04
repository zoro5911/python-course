def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return (num * factorial(num-1))

print(factorial(3))
print(factorial(4))
print(factorial(5))

#Another Example:-
def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return (num * factorial(num-1))

#Driver Code

num = 7
print("Number: ", num)
print("Factorial: ", factorial(num))


#quick quiz answer:-

def f(num):
    if(num == 0):
        return 0
    elif (num == 1):
        return 1
    elif (num == 2):
        return (f(1) + f(0))
    else:
        return (f(num-1) + f(num-2))

#Driver Code
num = 6
print("Number: ", num)
print("Fibonacci sequence: ", f(num))


