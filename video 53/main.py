# # Map 
# def cube(x):
#     return x * x * x

# print(cube(2))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))

# newl = list(map(cube, l))

# print(newl)

# # FILTER 
# def filter_function(a):
#     return a>2
# newnewl = list(filter(filter_function, l))
# print(newnewl)

from functools import reduce 

#list of numbers
numbers = [1, 2, 3, 4, 5]

#calculate the sum of the nubers using the reduce function
def mysum(x, y):
    return x + y 

sum = reduce(mysum, numbers)

#print the sum
print(sum)



