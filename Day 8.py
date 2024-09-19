#f - string == string format
 
user_name = input("")
age = input("")
birthday = input("")
greeting_msg = "Hello, " + user_name + ". Your age is" + age \
    + ". and your bd is" + birthday + "."

greeting_msg_formatted = f"""Hello, {user_name}, Your age is {age} and your bd is {birthday}."""
print(greeting_msg_formatted)


# spliting
print(greeting_msg_formatted.split("e"))


#in / not in operators



s = "I want to sleep"
print("k" in s) # check that we have it or not
if " " not in s or s[4] == "v":
    print("YEY")
elif s[3] == "w":
    print("wow")
else:
    print("Nah")

result = s.count("to") #counting that how many we have that charactor or words
print(result)

s.capitalize() # only first cha
s.upper() # all
s.lower() # all
s.isupper() # check if the sentence is All upper. Again, "A L L" of the sentence

s.replace("", "") # 1st = the one we choose, 2nd = the one we want it to replace

# Loop by character

for character in s:
    print(character)

# Loop by index
    for i in range (15):
        print(s[i])

    for i in range (15):
        print(i, s[i]) # the amount can be less but not more than the real amount

# slope the problem
for i in range (len(s)):
        print(s[i])

#Enumarate == give both index and character like the (i, s[i])
for i , character in enumerate:
        print(i, character) # if we switch, it switches






