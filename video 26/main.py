import time
t = time.strftime('%H:%M:%S')
print(t)


hour = int(time.strftime('%H'))
print(hour)

if(hour>0 and hour<12):
    print("Good Morning Sir")
elif(hour>12 and hour<4):
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")





