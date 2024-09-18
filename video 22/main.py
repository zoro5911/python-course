# marks = [3, 5, 6, "Harry", True, 8, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# # Same thing applies for strings as well!
# if "ar" in "Harry":
#   print("Yes")
# else:
#   print("andha hai kya") 

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:11:4])

lst = [i*i for i in range(11)]
print(lst)
lst = [i*i for i in range(11) if i%3==0]
print(lst)