# *Ards, **kwargs
def add (a, b, c, d):
    return a+b+c+d

def add(*ards):
    print(*ards)
add(1, 2, 3, 4 , 5) #Horizontal

def add(*ards):
    for element in ards:
        print(element)

add(1, 2 ,3) # Vertical

def add(*ards):
    result = 0
    for element in ards:
        result += element
    return result
    print(result)

add(1, 2 ,3) # Vertical

# **kwargs == dictionary of the variable >> 
def greeting(pin=1, oi=2, **kwargs):
    print('hello', pin, oi, kwargs['rin']) #kwargs['rin'] will print 2

greeting(rin=2, Samu=10, tsumu=7) 

#Literal

def square(x:float): #specified type of thing
    return x ** 2
print(square)

def multiply_three_num(a: float, b: float, c: float) -> float:
    return a * b * c
print(multiply_three_num)

def get_first_cha(s):
    return s[0]
print(get_first_cha("Pin")) #P

def lower_first_cha(s: str):
    return s.lower()
print(lower_first_cha("Pin")) # pin



