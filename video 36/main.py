# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")

# try:
#     for i in range(1, 11):
#       print(f"{a} x {i} = {int(a)*i}")
# except:
#    print("invalid input")

# print("some imp lines of code")
# print("End of program")

#More Examples:-

try:
   num = int(input("Enter an integer: "))
   a = [6, 3]
   print(a[num])
except ValueError:
   print("That's not an integer!")
except IndexError:
   print("Index out of range!")
