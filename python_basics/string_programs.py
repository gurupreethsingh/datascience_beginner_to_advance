"""
String can be made in 3 ways
1. single quotes
2. double quotes
3. either 3 single quotes or 3 double quotes ( these are called as doc strings or document strings)
"""

s1 = 'Hello Ecoders'
s2 = "Hello Ecoders"

s3 = """Hello ecoders 
welcome to python , Data Science classes
"""

print(type(s1))
print(type(s2))
print(type(s3))

print()
print("*"*40)

print(len(s1))
print(len(s3))

print()
print("*"*40)
print("Printing all the strings")
print(s1)
print(s2)
print(s3)


print()
print("*"*40)
print("Printing string using for-loop using 'in' operator")
for i in s1:
    print(i, end="")

print()
print("*"*40)

print("Printing string using for-loop using the range() function ")
for i in range(0, len(s1)):
    print(s1[i], end="")

print()
print("*"*40)
print()

print("Printing string from start to end using the index values and brackets")
print(s1[:])
print(s1[0:])
print(s1[0:len(s1)])
print(s1[::])
print(s1[::1])

print()
print("*"*40)
print("Printing everything from a specific index value ( slicing) ")
print(s1[6:])
print(s1[6: len(s1)])
print(s1[6:10])    # this will print only from 6th to 9th index values
print("*"*40)
print()
print("Printing / slicing using negative index")
print(s1[-13: -1])
print(s1[-5])

print()
print("*"*40)
print("printing string by slipping one , one digit in between")
print(s1[::1])

print()
print("*"*40)
print("Printing 2 digits in between")
print(s1[::3])
print(s1[0:len(s1):3])

print()
print("*"*40)
print("Printing string in reverse")
print(s1[::-1])

print()
print("*"*40)
print("String functions")
s2 = "StringFunctions"
print(s1.capitalize())
print(s1.islower())
print(s1.isupper())
print(s1.isdigit())
print(s1.isalpha())
print(s2.isalpha())

print(s1.isalnum())
s3 = "abc123"
print(s3.isalnum())

print(s1.isnumeric())
s4 = "123354345"
print(s4.isnumeric())

print(s1.istitle())
s5 = "stringfunctions"
print(s5.istitle())

print(s1.lower())
print(s1.upper())
print(s1.swapcase())
print(s1.casefold())
print(s1.casefold())

s6 = "ECODERS"
print(s6.casefold())

print()
print("*"* 40)
print("using 'in' and 'not in' operators to find the elements inside the strings")

if "f" in s1:
    print(s1.index("f"))
else:
    print("not found")

print()
print("*"* 40)

if 's' not in s1:
    print("Not present")
else:
    print(s1.index('s'))

print()
print("*"* 40)
print("Priting how many times a variable comes in the string")
s1 = "welcome Ecoders to data science class"
print(s1.count("s"))

