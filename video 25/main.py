tuple1 = (0, 3, 1, 2, 2, 31, 1, 3, 2, 3, 5)
res = tuple1.count(3)
print('Count of 3 in tuple1 is:', res)
# res = tuple1.index(3)
# res = tuple1.index(31)
res = tuple1.index(3, 4, 8)
print('index of 3 in tuple1 is:', res)
res = len(tuple1)
print('The length of tuple is:', res)


#More Examples

countries = ("Pakistan", "Afghanistan",
             "Bangladesh", "Srilanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

countries = ("Spain", "Italy", "India",
             "England", "Germany")
temp = list(countries)
temp.append("Russia")    #add item
temp.pop(3)              #remove item
temp[2] = "Finland"      #change item
countries = tuple(temp)
print(countries)

#count() Method
Tuple1 = (0, 1, 3, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
res = Tuple1.index(3)
print("First occurence of 3 is:", res)
