#Set is having 12 methods add(x), update(iterable), remove(x), discard(x), pop(), clear(), union(t), intersection(t), difference(t), issubset(t) and issuperset(t) check below how these methods are used

#Set without element
# s = set()

#Set with one element
# s={1} or s={"Shashank"} or s={a} or s={3.5}

#List with one element using constructor
# s = set([10])

# s={1}
# print(type(s))

# #below we can see the add() example here add method can add only one value and the adding place is random because set is unordered data type
# S={1, 2, 3, 5, 6, 7, 8}
# S.add(4)
# S.add(9)
# S.add(10)
# print(S)

# #below we can see the update() example update method can add multiple value at same time
# S={1, 2, 3, 5, 6, 7, 8}
# S.update([4,5,6])
# print(S)

# #below we can see the remove() example remove() will give key error if given element not found
# S={1, 2, 3, 5, 6, 7, 8}
# S.remove(2)
# print(S)

# #below we can see the discard() example discard() will not give any error if given element not found
# S={1, 2, 3, 5, 6, 7, 8}
# S.discard(2)
# print(S)

# #below we can see the pop() example pop() will remove the random value
# S={1, 2, 3, 5, 6, 7, 8}
# S.pop()
# print(S)

# #below we can see the clear() example clear() will remove all the elements present inside the set and return empty set
# S={1, 2, 3, 5, 6, 7, 8}
# S.clear()
# print(S)

# #below we can see the union() example union() will Combine both sets and remove all the duplicate elements
# S={1, 2, 3}
# S1={3, 4, 5}
# S3=set()
# S3.update(S.union(S1))              #we cant use Add method here because set allows only immutable objects inside to add
# print(S3)

# #below we can see the intersection() example intersection() will put only common values of both sets
# S={1, 2, 3}
# S1={3, 4, 5}
# S3=set()
# S3.update(S.intersection(S1))
# print(S3)

# #below we can see the difference() example difference() will only put unique values of first set
# S={1, 2, 3}
# S1={3, 4, 5}
# S3=set()
# S3.update(S.difference(S1))
# print(S3)

# #below we can see the symmetric_difference() example symmetric_difference() will only put unique values of both set
# S={1, 2, 3}
# S1={3, 4, 5}
# S3=set()
# S3.update(S.symmetric_difference(S1))
# print(S3)