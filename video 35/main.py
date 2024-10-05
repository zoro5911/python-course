i = 0
while i < 10:
    print(i)
    i = i + 1
else:
    print("Sorry no i")


i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 5:
        break
    #as we can see the data under else is not printed because else is printed when loop ends or is completed not when the loop is breaked

else:
    print("Sorry no i")

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of Loop")

