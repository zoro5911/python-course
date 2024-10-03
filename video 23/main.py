# l = [11, 45, 1, 2, 4, 6,]
# print(l)
# # l.append(7)
# # l.sort(reverse=True)
# # l.reverse()
# # print(l.index(1))
# # print(l.count(1))
# # m = l.copy()
# # m[0] = 0
# l.insert(1, 899)
# m = [900, 1000, 1100]
# k = l +m
# print(k)
# # l.extend(m)
# print(l)

# More Examples
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse = True)
print(colors)


num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse = True)
print(num)

colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)


num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,2,8,9,7]
print(num.index(3))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,1,5,3,6,1,2,1,2,8,9,7]
print(num.count(1))

colors = ["voilet", "indigo", "blue", "green"]
newlist = colors.copy()
print(colors)
print(newlist)

colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]
colors.insert(1, "green")  #inserts item
# at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#             indexes      [0]      [1]       [2]      [3]
print(colors)

#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange","red"]
colors.extend(rainbow)
print(colors)

# concatenating two lists:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)