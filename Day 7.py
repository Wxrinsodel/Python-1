#nested loop

first_num = int
second_num = int

for first_num in range(5):
    for second_num in range(6):
        print(first_num,second_num)

for i in range(2, 5):
    for j in range (2, 6, 2): # 2 - 6 เพิ่มทีละ2
        print(i, j)

#string

empty_string = ""
empty_string = """"""
empty_string = ''
empty_string = str()

s1 = "Hello, " #เว้นช่องเอาเอง
s2 = "World"
print (s1 + s2)

s3 = """
I love money
I love money
I love money
I love money
I love money
"""
print(len(s3)) #the lenght of sentence


# Indexing
"""
s = ""
print(s[34])
"""

# slicing

oi = "Hello, world!"
print(oi[6:8]) # 6th till 7th

"""
a1 = (a,b,c) # start, stop, step
"""

