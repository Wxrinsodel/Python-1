#Loop & for loop == for loop is you know how many time you want to loop

#Loop

"""
While CONDITION:
    print()

ex. while Ture:
    print("Hello") >> it will run until the computer can not handle
"""

number = 1
while number <= 20:
    print(number)
    number += 1

number = 1 
while True:
    print(number)
    if number % 3 == 0 and number % 2 == 0:
        break
    
    if number == 2:
        continue
    
    if number == 1:
        pass
    number += 1

 #for loop >> range(start,stop,step)

range(6) # 1-5
range(2,5) # start w/ the lessen number (3,4)

range(10,-1,-1) # start 10 to 0

number = 1
for number in range(5):
    print(number)

for number in range(28, 5, -3):
    if number % 2 == 0:
        print(number)

for number in range(1,11):
    square = number ** 2
    print(square)


