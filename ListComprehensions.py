mystring = "hello"

# Make a list of letters in a string
mylist = []

#for letter in mystring:
#    mylist.append(letter)

# 1 line method

mylist = [letter for letter in mystring]


# Make a list of numbers and then do something with the numbers

mylist2 = [num for num in range(0,11)] # Make list 0 1 2 3 4 .......
mylist2 = [num**2 for num in range(0,11)] # Get square of every number
mylist2 = [num for num in range(0,11) if num%2==0] # Print only even numbers

print(mylist2)

