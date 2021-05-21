#Tokens :- the smallest part of any programming language
"""
1. identifiers
2. literals
3. variables
4. keywords
5. separators
6. operators
"""

# identifiers :- are the names given to our variables and programs

a = 10  # we have given 'a' as the name to identify the integer value 10
print(a)

#literals :- are the types of variables, the different data types
a = 10   # interger type of literal
b = 23.4   # float( decimal) type of literal
c = 'a'    # character or string type of literal
d = 'hello welcome to data science'   # string literal
f = "welcome ecoders"   # string literal

#variables:- variables are the named memory location, which can store any type of data and that data can be change during the execution of the program.

a = 20    # we have named the memory location as 'a' where 20 is stored.

# keywords :- are the reserved words in python. we cannot use the keywords as our variable names.

# there are 36 keywords in python.
# we can print all the keywords, by first importing the keyword library and next in print() function type keyword.kwlist

import keyword
print("pythons keywords are:- ")
print(keyword.kwlist)

# to print the total number of keywords we can use the len() function
print(len(keyword.kwlist))

"""
pythons keywords are:- 
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
36
"""

# separators :-  the separators used in python are
'''
1. () paranthesis :- used for making sets and tuple.
2. [] brackets :- are used for making list.
3. {} brases :- are used for making dictionary.
4.  :  colon
5.  ;  semi-colon
6,  .   dot/ dot operator
'''

# 6. operators :- operators perform some operations on operands .
'''
1. arithematic operator :-
   + for addition
   -  for subraction 
   *   for multiplication 
   **   for power of a number
   /    for division , to get floating point answer
   //   for division  , to get integer part as answer
   %    modulus operator is used to get the reminder,
'''

a = 7
b = 2

print(a+b)   # 9
print(a-b)   # 5
print(a*b)   # 14
print(a**b)  # 49
print(a/b)   # 3.5
print(a//b)  # 3
print(a % b)   # 1

'''
2. relational operators :- 
    <    less than 
    >    greater than
    <=   less than or equal to
    >=   greater than or equal to 
    ==   equal to equal to 
    =    assignment operator
    !=   not equal to
    <>   not equal to 
'''

a = 10
b = 2
c = 10
print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a == c)

"""
incremental and decremental operator
+=  incremental operator
-=  decremental operator
"""
a = 2
a += 1
print(a)

a -= 1
print(a)

a *= 2
print(a)

a //= 3
print(a)
