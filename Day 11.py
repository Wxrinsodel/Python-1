# Function Structure
def function_name():
    # What you do
  
def print_greeting():
    """
    This function will print hello for 3 times.
    """
    print('Hello')
    print('Hello')
    print('Hello')

# input and output
def greet_person(person_name):
    """
    Receive the name of a person and print out the greeting
    sentence.
    """
    print(f'Hello, {person_name}.')

def give_me_number_3():
    return 3

# parameter
def calculate_price(number_of_apple):
    apple_price = 60
    return number_of_apple * apple_price

# Argument
total_price = calculate_price(4)
print(f'The total price is {total_price}')

# Multiple Outputs
def give_me_3_and_5():
    return 3, 5
print(give_me_3_and_5())

numbers = give_me_3_and_5()
print(numbers[0] * 5)

first_num, second_num, third_num = (1, 2, 10)
print(third_num) #10
number1, number2 = give_me_3_and_5()
print(number1) #3
print(number2)#5

# Multiple Inputs
def add_two_number(first_num, second_num):
    return first_num + second_num
print(add_two_number(3, 5)) #8


#number = 20
def calculate_price_v2(num_apple, apple_price=50):
    return num_apple * apple_price
  
#calculate_price_v2(3, 40)
calculate_price_v2(num_apple=10, apple_price=20) #200

# calculate_price_v3(3, 2, 60, 10)
calculate_price_v3(3, 2)
# positional arguments, keyword arguments
# positional before keyword
calculate_price_v3(3, 5, banana_price=70)

calculate_price_v3(3, num_banana=2, banana_price=70) #290
calculate_price_v3(3, banana_price=70, num_banana=2) #290



