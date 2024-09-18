# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)

# average(4,6)  

# def average(*numbers):
#   # print(type(numbers))
#   sum = 0
#   for i in numbers:
#     sum = sum + i
#   print("Average is: ", sum / len(numbers))
#   return 9
#   return sum / len(numbers)


# c = average(5, 6, 9, 7)
# print(c)


def name(**name):
  # print(type(name))
  print("Ram Ram,", name["fname"], name["mname"], name["lname"])


name(mname="Singh", lname="Sura", fname="Aditya")