# Map function

def square(num):
    return num**2

myNums = [1,2,3,4,5]

# Print nums squared one by one
for item in map(square,myNums):
    #print(item)
    pass

# Print nums squared in a list / Put them in a list
#print(list(map(square,myNums)))

def splicer(s):
    if len(s) % 2 == 0:
        return 'Even'
    else:
        return s[0]

names = ['Raven','Lana','Jyn','Rey']

#print(list(map(splicer,names)))

# Filter function

def checkEven(num):
    return num % 2 == 0

myNums = [1,2,3,4,5,6]

#print(list(filter(checkEven,myNums)))

# Lambda expressions

# Before
def square2(num):
    result = num ** 2
    return result

# After
lambda num: num ** 2

# Assign it
square3 = lambda num: num ** 2

# Example of using lambda instead of making a whole function

print(list(map(lambda num: num ** 2,myNums)))

print(list(filter(lambda num: num % 2 == 0,myNums)))

print(list(map(lambda name: name[0],names)))

print(list(map(lambda name: name[::-1],names)))