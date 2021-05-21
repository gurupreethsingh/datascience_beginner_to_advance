'''
Conditional statements in python :-
1. if
2. if-else
3. elif
3. break
4. continue
'''

# taking string input from the user, using the input() function
name = input("enter your name")
if name == "john":
    print("welcome " + name)
else:
    print("No access")


# elif condition
if name == "john":
    print("Welcome "+ name)
elif name == "snow":
    print("Welcome "+ name)
else:
    print("Access Denied")


# loop control statements :-
# range() function
# while loop
# for loop

# while loop
print()
print("*" * 40)
a = 1

while a <= 10:
    print(a)
    a += 1

print()
print("*" * 40)

a = 10
while a >= 1:
    print(a)
    a -= 1

print()
print("*" * 40)
print(range(1, 10))

print()
print("*" * 40)
for i in range(1, 11):
    print(i)

print()
print("For horizontal alignment of printing , we will put end=''  at the end")
for i in range(1, 11):
    print(i, end=" ")

print()
print("Printing numbers in reverse")

for i in range(10, 0, -1):
    print(i, end=" ")


print()
print("*" * 40)
print("printing even numbers , using range() function")
for i in range(1, 11, 2):
    print(i, end=" ")

print()
print("*" * 40)
print("Skipping two digits from the series")

for i in range(1, 100, 3):
    print(i, end= " ")

print()
print("*" * 40)

print("printing multiples of 5")
for i in range(5,51, 5):
    print(i, end=" ")

print()
print("*" * 40)
print("printing multiplication table")

num = int(input("enter the number"))
for i in range(1,11):
    print(str(num) + " * " + str(i) + " = " + str(num*i))

print()
print("*" * 40)

print("break keyword")

for i in range(1, 11):
    print(i, end=" ")
    if i == 5:
        break

print()
print("*"* 40)

print("continue keyword, will skip the condition given in if-condition")
for i in range(1,11):
    if i == 5:
        continue
    print(i, end=" ")


print()
print("*"* 40)

for i in range(1, 11):
    if i >= 4 and i<= 7:
        continue
    print(i, end=" ")



