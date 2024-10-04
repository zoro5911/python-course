dic = {
    344: "Aditya",
    678: "Zakir",
    56: "Arshdeep",
    567: "Vivian"
}

print(dic[344])

#More Examples:-
info = {'name':'Aditya', 'age':'19', 'eligible':True}
print(info)
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

#1. Accessing single values:
info = {'name':'Aditya', 'age':'19', 'eligible':True}
print(info['name'])
print(info.get('eligible'))

# print(info['name2'])  use this if you want to throw an error
# print(info.get('eligible')) use this if you don't want to throw error'

#2. Accessing multiple values:
info = {'name':'Aditya', 'age':'19', 'eligible':True}
print(info.values())

# 3.Accessing keys:
info = {'name':'Aditya', 'age':'19', 'eligible':True}
print(info.keys())

# 4.Accessing key-value pairs:
info = {'name':'Aditya', 'age':'19', 'eligible':True}
print(info.items())



