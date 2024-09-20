#list

word = input()

num_of_word = len(word)
for i in range (len(word)):
    if word[1] != word[num_of_word - i - 1]:
        print("NO")
        break
else:
    print("YES")

l = [1, 2, 8, None, "Pin"]
#print((l[3]) ='g')


#list extractor
l = [1, 2, 8, None, "Pin", print]
print(l) # have []
print(*l) # have no []

zeroes = [0] * 5
plus = [3] + [2]
print(plus)

#Sort == min to max (arrange)

#l.sort(reverse=True)

# in 2 not in
s = "Teerak tor"
print('v' in s)

t = [1, 3 ,6 , None]
print([1, 3 ] in t) # it's include[]
print(3 in t)

# add if else elif, List conditional
t = [1, 3 ,6 , None]
if 3 in t:
    print("YES")
else:
    print("NO")    

#Loops
s = "Teerak tor"


p =[1 , 2.5, 3.5]
print(list(map(int, p)))
print(list(map(str, p)))

# we want list of [1, 2, 3, 4, 5] > map
p = list(map(int, input().split())) #give you your typing thing out


#TUPLE == list that cannot change, add ,delete
empty_list = [ ]
empty_tuple = { } 

r = (1, 2, 3)
print(type(r))

one_element_list = [2]
one_element_tuple = (2,) # (2) will be int

print(type(one_element_tuple))

#### tuple cannot append, sort but can be "sorted" ####

#convert tuple to list
r = (1, 2, 3)
