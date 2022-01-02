print("hello world")

#functions and assigning variables
def hello():
    print("hello word in a function")
hello()

hi = "before hello was changed"

def returning():

    hi = "hello world in a variable that has been returned and changed"
    return hi

returning()
print(hi)
print(returning())
hi = returning()
print(hi)

#user input
#normal
disctag = input("what is your full discord tag: ")

#optimised with error catching
#input split with a space
def bySpace():
    try:
        name, tag = input("enter your name and tag split by a space: ").split()
        print("name: ", name)
        print("tag: ", tag)
        return name, tag

    except ValueError as e:
        print ('Value Error: re-enter values: \n')
        bySpace()
#bySpace()
name,tag = bySpace()
#print("name is: ",name)

def byComma():
    try:
        name2, tag2 = input("enter your name and tag split by a comma: ").split(",")
        print("name: ", name2)
        print("tag: ", tag2)
        return name2, tag2

    except ValueError as e:
        print ('Value Error: re-enter values: \n')
        byComma()
#byComma()
name2,tag2 = byComma()


#dictionaries
tags = {name:tag, name2:tag2}
print(tags)
print(tags[name2])
print(len(tags))
print(type(tags))

#but why a dictionary
k = tags.keys()
print(k)
v = tags.values()
print(v)

#change values in a dictionary
tags[name] = "beans"
print(tags[name])
print(tags)