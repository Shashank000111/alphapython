###################################### Simple If Else #########################################################
#WAP to check if the given character is a special character
a=input("Input character:")
if not a.isalnum():
    print(f"{a} is a special character")

#WAP to check if the iterable is empty or not
l=[1,2,3]
if l:   # bool(l)   ==>   If l is not empty means bool value "True"   ==>    If l is empty means bool value "False"
    print("l is not empty")
else:
    print("l is empty")

#WAP to check if the key is present in the dictionary or not
d={"a":1, "b":2, "c":3}
key='a'
if key not in d:
    print(f"{key} key is not present is d")
else:
    print(f"{key} key is present is d")

###################################### in Line if #############################################################

# Syntax =>  { if condition: statement1; statement2....etc }
# ***Warning***  in line if cant be written inside the print()

a=3
if a < 5 and a % 2 != 0: print("a is lessthen 5"); print("a is odd number")

###################################### in Line if else ########################################################

# Syntax =>  { (True Block) if condition else (false block) }
# ***Advise*** this could be write in side the print()

#WAP to check if the value of number is greater or not
number=3
print("grater" if number>1 else "not grater")

#WAP to check if the key is present in the dictionary or not
d={"a":1, "b":2, "c":3}
key='a'
print(f"{key} key is not present is d" if key not in d else f"{key} key is present is d")

#WAP to check if the value is string or not
s = "Shashank"
print("Value is string" if isinstance(s,str) else "value is not string")

#WAP to check if the last letter of value is vowel or not
s = "Shashank"
print("Value is vowel" if s[-1] in ("A","E","I","O","U","a","e","i","o","u") else "value is not vowel")


