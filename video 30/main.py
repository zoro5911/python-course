# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
# def factorial(n):
#   if (n == 0 or n == 1):
#     return 1
#   else:
#     return n * factorial(n - 1)


# print(factorial(5))
# print(factorial(4))
# print(factorial(3))
# print(factorial(2))
# print(factorial(1))
# print(5 * 4 * 3 * 2 * 1)

# Quick Quiz: Write a program to print the Fibonacci sequence

#answer

def f(n):
  if (n == 0):
    return 0
  elif(n == 1 or n == 2):
    return 1 
  else:
    return  f(n-1) + f(n-2)

n = 10 # Assign a value to n

# Print the Fibonacci sequence up to n

for i in range(n + 1):
  print(f(i))

# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....