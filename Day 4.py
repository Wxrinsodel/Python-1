# Not and Or

ab = not True # not is not a function
cd = not False 

print(cd)

a = True and True
b = False and True #False
c = False and False

# all statement are true == True
print(a)

d = True or True
e = False or True
f = False or False

print(e)

g = 5
h = 6
print(g != h-1 or h ** 2 > g)


#Adder Program



first_number = int(input("Enter your first nunber:"))
second_number = int(input("Enter your second_number nunber:"))
added_result = first_number + second_number
print(added_result)

# Task -- Celcius to Fahrenheit


celcius = float(input("Enter your temperature in celcius : "))

fahrenheit = (celcius * 9 / 5) + 32

kelvin = celcius + 273

print("Your temperature in Fahrenheit is", fahrenheit, "and in Kelvin is", kelvin)


# Math 

"""

abs = 1.0 # absolute
max(23, 6, 9, 0, -3) # find a max
min(8,0,-4,-56) # find a min
round(2.45, 1) #ปัดเศษ
round(-1.537, 3)
print()

"""
