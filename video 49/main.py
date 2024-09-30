# Reading a file 

# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# Writing in a file

f = open('myfile.txt', 'a')
f.write('Hello, world!')
f.close()

with open('myfile.txt', 'a') as f:
  f.write("hey i am inside width")