with open('file.txt', 'r') as f:
    print(type(f))
    #Move to the 10th byte in the file 

    f.seek(10)

    #Read the next 5 bytes
    print(f.tell())
    data = f.read(5)
    print(data)

#Truncate

with open('sample.txt', 'w') as f:
    f.write('Hello, World3!')
    f.truncate(4)

with open('sample.txt', 'r') as f:
    print(f.read())