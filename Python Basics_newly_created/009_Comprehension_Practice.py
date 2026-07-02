###############  List Comprehension  ################

#Syntax ==>>  [expression for item in list]

#WAP to create a list of square of number using comprehension
l=[1,2,3,4,5]
l1=[i**2 for i in l]
print(l1)

#WAP to print even number from 1 to 50 using comprehension
l1=[i for i in range(1,50) if i%2==0]
print(l1)

#WAP to print even number from 1 to 50 using comprehension
l1=[i for i in range(1,50) if i%2==0]
print(l1)

#WAP to create a list with words if even length add it as it else reverse and add.
s="hello everyone it is thursday"
l=s.split()
l1=[i[::-1] if len(i) % 2==0 else i for i in l]
print(l1)

#WAP to create a list of elements which are starting with vowel
s=["laura", "steve", "bill", "james", "bob", "george", "scott", "alex", "ive" ]
l=[i for i in s if i[0] in "AEIOUaeiou"]
print(l)

#WAP to filter all the languages which starts with p
s=["python", "java", "perl", "php", "js" ]
l=[i for i in s if i[0] == "p"]
print(l)

#WAP to create a list of elements which are starting with consonant
s=["laura", "steve", "bill", "james", "bob", "george", "scott", "alex", "ive" ]
l=[i for i in s if i[0] not in "AEIOUaeiou"]
print(l)


#WAP to filter out the names which are less than 6 characters
s=["laura", "steve", "bill", "james", "bob", "george", "scott", "alex", "ive" ]
l=[i for i in s if len(i)<6]
print(l)

#WAP for raise a power of list index
l=[1,2,3,4,5]
l1=[v**i for i,v in enumerate(l)]
print(l1)

#WAP to build a list of tuple with string and its length pair.
s=["laura", "steve", "bill", "james", "bob", "george", "scott", "alex", "ive" ]
l=[(i,len(i)) for i in s]
print(l)

#WAP to build a list of tuple with string and its length pair if the length is even.
s=["laura", "steve", "bill", "james", "bob", "george", "scott", "alex", "ive" ]
l=[i for i in s if len(i)%2==0]
print(l)

#WAP to generate list of PI values with increasing decimal point numbers
##### First Method
import math
PI=math.pi
print(PI)

##### Second Method
n=10
PI=3.1457
l=[round(PI,i) for i in range(1,10)]
print(l)

#WAP for list of comprehension to sum the factorial of numbers from 1 to 5

#   1   1 x 1                   1
#   2   2 x 1                   2
#   3   3 x 2 x 1               6
#   4   4 x 3 x 2 x 1           24
#   5   5 x 4 x 3 x 2 x 1       120

#First Method
from math import factorial
l=[factorial(i) for i in range(1,6)]
print(sum(l))

#Second Method
fact=1
l=[]
for i in range(1,6):
    fact=fact*i        #1 2 6 24 120
    l.append(fact)
print(l)
print(sum(l))

###############  Dict Comprehension  ################

#Syntax ==>>  [key:value for item in iterable]

#WAP to create a dict with words and its length value
s="hello good morning"
d={i:len(i) for i in s.split()}
print(d)

#WAP to create a dict with words and its length value
s="hello good morning"
d={i:len(i) for i in s.split()}
print(d)

#WAP to create a dict with words and its length value only if it is even length
s="hello good morning"
d={i:len(i) for i in s.split() if len(i)%2==0}
print(d)

#WAP to print index and its word pair if the word is even length keep it as it is else reverse it
s="hello good morning"
d={ i:v if len(v)%2==0 else v[::-1]  for i, v in enumerate(s.split())}   # remember we don't write key in else block
print(d)

#WAP to create a dictionary with character and its ascii value.
s="hello world"
d={i:ord(i) for i in s}
print(d)

#WAP to reverse the value in dict if the type of value is string reverse it
d={'a':1, 'b':"hello", 'c':85, 'd':12.3, 'e':[1,2,3]}
d1={key:value[::-1] if isinstance(value,str) else value for key,value in d.items()}
print(d1)

#WAP to create a dict with words and count pair
s="hello how are you hi hello hi hello"
l=s.split()
d={i:l.count(i)for i in l}
print(d)

#WAP tp flip the keys values of the dictionary using dict comprehension
d={'a':1, 'b':"hello", 'c':85, 'd':12.3, 'e':(1,2,3)}
d={v: k for k, v in d.items() if isinstance(v, (int, float, str, tuple))}
print(d)

#WAP to convert two list in to dict
l1=["hello", "world"]
l2=[10, 20]
d={k:v for k,v in zip(l1,l2)}
print(d)

#WAP to group odd and even number given in the below list
items=[1,2,3,4,5,6,7]
from collections import defaultdict
d=defaultdict(list)
for i in items:
    if i%2==0:
        d[0].append(i)
    else:
        d[1].append(i)
print(d)


