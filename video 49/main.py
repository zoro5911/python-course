#Reading A File

f = open('myfile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()

#Writing to a File

f = open('myfile.txt', 'a')
f.write('hello, world!')
f.close()

with open ('myfile.txt', 'a') as f:
    f.write("Hey I am inside with")
