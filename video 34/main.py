ep1 = {122: 45, 123: 89, 567: 68, 678: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
ep1.popitem()
# ep1.pop(122)
del ep1[122]
print(ep1)

#More Examples
#update():-
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

#removing items from dictionary:
# clear():-
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)
#pop():-
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
#popitem():-
info = {'name':'Karan', 'age':19, 'eligible':True}
info.popitem()
print(info)
#del:-
info = {'name':'Karan', 'age':19, 'eligible':True}
del info['age']
print(info)

# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
#  del info #If key is not provided, then the del keyword will delete the dictionary entirely.
# print(info)

# output:- NameError: name 'info' is not defined





