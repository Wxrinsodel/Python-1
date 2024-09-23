# Set (union, intersection,different)
empth_set = set()
non_empth_set = {1, 2, 3}
print(non_empth_set)


#union
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.difference(b)) # a - b = error because it's a set??????
print(a.intersection(b))
print(a-b) #WTF it's like an exception for set

#changing set
a.remove(2)
print(a) # {1, 3}
b.add(9)
print(b) #{9, 3, 4, 5}

#Dictionary

empty_dict = {}
empty_dict = dict()

animals_legs = {'horse': 4, 'human': 2, 'fish': 0, 'idk' :[1, 2], 'zero' : [0]}

# d = {[1, 2]: 'No'} # can not use set as a dictionary key
d = {(1, 2): 'no'} #work

# CALLING DICTIONARY

animals_legs = {'horse': 4, 'human': 3, 'fish': 0, 'idk' :[1, 2], 'zero' : [0]} # change then change
print(animals_legs['horse']) # house is variable >> output is 4
print(animals_legs)

# Change the value

animals_legs['horse'] = 6
print(animals_legs) # overwrite the value

print(len(animals_legs)) #count in pairs

# in/not in

print("horse" in animals_legs) # True for variable ( the first before :)

#Methods

animals_legs = {'horse': 4, 'human': 3, 'fish': 0, 'idk' :[1, 2], 'zero' : [0]}
print(animals_legs.get('horse')) # this one is more safe, use it


