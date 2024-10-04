letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Aditya"

print(letter.format(name, country))

# letter = "Hey my name is {} and I am from {}"
# country = "India"
# name = "Aditya"
#
# print(letter.format(country, name))
#this will give output :- Hey my name is India and I am from Aditya
#which is not desired
#we can fix that by this way:-

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Aditya"

print(letter.format(country, name))
#this will give the desired output

#Here's Another Way:-

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Aditya"

print(letter.format(country, name))
print("Hey my name is {name} and I am from {country}") #OOOPS! this is not showing the desired output so we will use f-string method
#The method is used as follows:-

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Aditya"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
#now it will show desired output thanks to f-string method

# if u want to use f-string method and show the curly braces item then us this method

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Aditya"

print(f"Hey my name is {{name}} and I am from {{country}}")
#now you can see the content inside the curly braces and all set!!!

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.099999))
#This can be done using another method (f-string method)

price = 49.099999
txt = f"for only {price:.2f} dollars!"
print(txt)

#More Examples
val ='Geeks'
print(f"{val} for {val} is a portal for {val}.")
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

print(f"{2 * 30}")
print(type(f"{2 * 30}"))



