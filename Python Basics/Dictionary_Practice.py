#Dictionary is having 11 methods get(), keys(), values(), items(), update(), setdefault(), fromkeys(), pop(), popitem(), clear(), copy() check below how these methods are used

#Dictionary without element
# d = {}    or   d = dict()

#Dictionary with one element
# Method                  Example
# {}                      {"a":1}
# dict() keyword          dict(a=1)
# tuple                   dict([("a",1)])
# zip                     dict(zip(["a", "b"],[1, 2]))    ==>> all keys inside one lista and all values inside another list
# fromkeys                dict.fromkeys(["a", "b"],1)   ==> when values are same for multiple keys {"a":1, "b":1}  all keys will share the same memory for values
# assignment              d["a"]=1   ==>> dynamic memory allocation we use this method on loops

#Dict with one element using constructor
# d = dict(a=1)
# print(d)

d = {'a': 1, 'b': 2, 'c': 3}
# print(d.get('a'))  # 1
# print(d.keys())    # ['a', 'b', 'c']
# print(d.values())  # ['1', '2', '3']
# print(d.items())   # [('a', 1), ('b', 2), ('c', 3)]

# d.update({'d':4})
# print(d)

# d.setdefault('a',0)
# d.setdefault('d',4)
# print(d)

# #fromkeys method always use inside the update method otherwise it will just only assign the values to keys but not add in empty dict
# d1={}
# d1.update(d1.fromkeys(['e','f','g'],0))
# print(d1)

# print(d.pop('a'))
# print(d)

# d.popitem()
# print(d)

# d2 = d.copy()
# print(d2)

# del d['a']
# print(d)
