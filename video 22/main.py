marks = [3, 5, 6, "Harry", True, 5, 7, 2, 32, 345, 23,]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) #Negative index
print(marks[len(marks)-3]) #Positive index
print(marks[5-3]) #Positive index
print(marks[2]) #Positive index

if 7 in marks:
    print("yes")
else:
    print("No")

print(marks)
print(marks[1:8])
print(marks[1:8:3])


lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
print(lst2[0])
print(lst2[1])
print(lst2[2])


details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
print(details[0])
print(details[1])
print(details[2])
print(details[3])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
  #        [0]     [1]      [2]      [3]       [4]
print(colors)
print(colors[2])
print(colors[4])
print(colors[0])

if "Yellow" in colors:
    print("Yellow is present")
else:
    print("Yellow is Absent")

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
  #       [-5]     [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

if "Orange" in colors:
    print("Orange is present")
else:
    print("Orange is Absent")

if "ity" in "Aditya":
    print("Yess sir")
else:
    print("no!")

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

#list comprehension
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

#More Examples
names = ["Milo", "Sarah", "Bruno", "Anastansia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastansia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
namesWith_O = [item for item in names if (len(item) == 4)]
print(namesWith_O)

