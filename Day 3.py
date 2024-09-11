# 1 -- Variable

age = 18
firstname = "Supawadee"
# make a change = just out a new information for the same variable 

"""
age = 17
firstname = "Oikawa"
print(age,firstname)

"""

date_of_birth = 16
month_of_birth = 9
year_of_birth = 2006

# Do not start the name of variable w/number and specific sign( . , < ) That's sh!t

# print(date_of_birth, month_of_birth ,year_of_birth, sep="\n")


# 2 -- INPUT Function always be string

"""

name_input = input("Please enter yout name:")
print("Hello, welcome", name_input)

"""
# 3 -- Converting data type

# int()
a = int("4")
a = int("-1")

"""
error type
1. a = int("True") 
2. a = int("2.4")   
3. a = int("-2.4")  cannot convert form negative float string.

"""


#print(a, type(a))

# Float
b = float("4")
b  = float("-1")
b = float("2.0")
b = float("-2.4")

#print(b, type(b))

# boolean
c = bool("4") #True
c = bool("-3") #True
c = bool("") #False
c = bool(None) # False

#print(c, type(c))


# string == can convert anything
d = str(1)
d = str(-5)
d = str(None)
d = str(True)
d = str(print()) #None

#print(d, type(d))

# Math Operations

a = 1 + 1
a = 1 - 1
a = 1 * 1
a = 1 / 1 # always in float os just add int infront == a = int(1 / 1) OR
a = 1 // 1 # result in integer
a = 2 ** 3 # quare
a = 7 % 3 # got a remain number from devide
# % == Modulus 
b = 7//3 # get just whole number
b = 34.9 % 3 # can do
b = 10 % 8.9 # can do too


"""
error type
1. 5 /0

"""
#print(b)

# int do something with float == float and float do something with float == float until find number
# Never get an exacty result from pthon when calculating

# 2. Order of operation == same as math

"""

a = 2 * 2 - 2 / 2 - 2 ** 2 # make it more clarify
b = (2 * 2) - ( 2 / 2 )- ( 2 ** 2 )# 1 st
c = 2*2 - 2/2 - 2**2 # 2nd
d = 4+5

"""


a = 4 + 4
b = 3 * 2
a = a + 4 # a = 8 it's run from the top
a = b

print(a)

#adjust 
a = 4 + 4
a = a + 6
print(a) # 14

a += 4 # 18
a -= 1 # 17

print(a)

# Logical Operators

a < 5
b > 4
c == 5
d >= 7
a <= 8
a != 9
