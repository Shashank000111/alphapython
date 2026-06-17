#Tuple is heaving 2 methods count() and index() check below how these methods are used

#Tuple without element
# t=()

#Tuple with one element
# t=(1, )

#Tuple with one element using constructor
# t=tuple("a")

#Tuple with brackets and without brackets
# t=(1, 2, 3, 4, 5, 2)
        #or
t = 1, 2, 3, 4, 5, 2


print(t.count(2))

#without arguments
print(t.index(2))

#with start index arguments
print(t.index(2, 1))

#with start and stop index arguments
print(t.index(2, 2, len(t)))

