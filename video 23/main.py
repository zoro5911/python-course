l = [11, 45, 7, 2, 4, 6, 7, 8]
print(l)
# l.append(7)
# print(l) 
# l.sort(reverse=True)
# print(l)  

# l.reverse()    
# print(l.index(7))
# print(l.count(7))  
m = l.copy()
m[0] = 0
l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
print(k)
# l.extend(m)
# print(l)