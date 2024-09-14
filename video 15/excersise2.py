import time

# Get the current time as a formatted string
timestamp = time.strftime('%H:%M:%S')
print(f"Current time: {timestamp}")
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# Extract the hour from the current time
current_hour = int(time.strftime('%H'))

# Greet based on the current hour
if 5 <= current_hour < 12:
    print("Good Morning")
elif 12 <= current_hour < 18:
    print("Good Afternoon")
else:
    print("Good Evening")
