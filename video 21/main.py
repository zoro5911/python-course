# def average(a = 9, b = 7):
#     print("The average is ", (a+b)/2)
#
# # average(4, 6)
# average(5)

# def name(fname, mname = "Singh", lname = "Sura"):
#     print("Hello,", fname, mname, lname)
# name("Aditya")
#
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name(mname="peter", lname = "Wesker", fname = "Jade")
#
# def name(fname, mname, lname="Quil"):
#     print("Hello,", fname, mname, lname)
# name("Peter", "ego",)

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum / len(numbers))
    # return 4
    return sum / len(numbers)

c = average(5, 6, 7, 8, 9)
print(c)

def name(*name):
    print("Moshi-Moshi, Oreva", name[0], name[1], name[2])
name("Monkey", "D.", "Luffy")