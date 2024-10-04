s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

#Joining sets
#1. union() and update():-
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Seoul", "Toronto", "almaty"}
cities3 = cities.union(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Seoul", "Toronto", "almaty"}
cities.update(cities2)
print(cities)

#2. intersection and intersection_update():-
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Toronto", "almaty"}
cities3 = cities.intersection(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Toronto", "almaty"}
cities.intersection_update(cities2)
print(cities)

#symmetric_difference and symmetric_difference_update():-
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Toronto", "almaty"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Toronto", "almaty"}
cities.symmetric_difference_update(cities2)
print(cities)

#difference() and difference_update():
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Toronto", "almaty"}
cities3 = cities.difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Toronto", "almaty"}
cities.difference_update(cities2)
print(cities)

#isdisjoint():
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Toronto", "almaty"}
print(cities.isdisjoint(cities2))

# issuperset():-

cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Toronto", "almaty"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

# issubset():
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Dubai", "brampton"}
print(cities2.issubset(cities))

#add():-
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities.add("Toronto")
print(cities)

#update():-
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

#remove():-
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities.remove("Madrid")
print(cities)

#pop():-
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
item = cities.pop()
print(cities)
print(item)

# #Del
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)
# NameError: name 'cities' is not defined We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

#clear():-
cities = {"Tokyo", "Madrid", "Dubai", "los angeles",
          "brampton"}
cities.clear()
print(cities)

#Check if item exists
info = {"Aditya", 19, False, 5.9}
if "Aditya" in info:
    print("Aditya is present")
else:
    print("Aditya is absent")









