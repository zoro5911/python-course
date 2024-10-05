try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("some erro occured")

finally:
    print("I am Always Executed.")

# now some will say we can print the above statement without using finally and yes you are right it will print the above statement:-
try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("some erro occured")


print("I am Always Executed.")

# but what about if we put the above code in a function?? let's see:-
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

#   finally:
#     print("I am always executed")
    print("I am always executed")
x = func1()
print(x)

# oops! it doesn't print I am always executed that's why we use as u can see below.:-
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
    # print("I am always executed")
x = func1()
print(x)

#More Example :-
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")


 
    