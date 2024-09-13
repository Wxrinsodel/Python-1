# if else function

if 5 < 7:
    print("True")

if not(5 != 4 and 6 < 3): 
    print("yes")

"""
if not 5 != 4 and 6 > 3 : 
    print("yes") 

this code is not print because the if function only affect to the first one

if not(5 != 4 and 6 > 3): 
    print("yes")
print("wow') > this one always print since it's out of the decision (thespace)

"""
if not 5 != 4 and 6 > 3 : #2nd
    if 6 > 5 : #1st
        print("Yes")
    print("yes") 
print("wow") # 3rd out of the command

if not 5 != 4 and 6 > 3 : #2nd
    if 6 > 5 : #1st
        print("Yes")
    print("yes") 
print("wow") # 3rd out of the command

# 1 if = 1 block of its
if 4 == 5:
    print("oh")
else: 
    print("Oh on")

if 7 != 9:
    print("Gogo let's go")
else:
    print("Nah")

#elif

if 2 > 5:
    print("yEs")
elif 3 > 4:
    print("Yes")
elif 4 > 3:
    print("yes")
else:
    print("sorry")

# which one is corrct > it's run.

#example

pocket_money = int(input("Enter your budget:"))
age = int(input("Enter your age:"))

if pocket_money > 3000:
    print("cavier and fori gras")
    if age >= 20:
        print("Wine")
if pocket_money > 1000:
    print("Sushi buffet")

