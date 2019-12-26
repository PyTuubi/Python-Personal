#  H e l l o
#  0 1 2 3 4
#  0-4-3-2-1


# single or double quotes
"hello"
'world'
"i'm yeetus"

#print("Hello")

#print("Hello \nworld!") #new line

#print("Hello \tworld!") #tab function

#print(len("Hello")) #len (length) function, includes spaces

string = "Hello World"

# Indexing
#print(string[0]) # = 0
#print(string[8]) # = r
#print(string[-1]) # = d
#print(string[-2]) # = l


# Slicing [start:stop:step]
# start = first letter wanted
# stop = up to, but don't include
# step = size of jump

#print(string[2:]) #from specific point to end
#print(string[:6]) #from beginning to specific point
#print(string[4:8]) #from specific point so another specific point
#print(string[::2]) #whole string but only every second letter
#print(string[::-1]) #reverse a string

# Immutability = Can't change 1 character of a string

name = "Jonni"
#name[5] = "a" # not possible

all_but_last = name[:-1]
#print(all_but_last + "a")

# can add strings and stuff together with +

letter = "F"
#print(letter * 10)

# Methods

x = "Hello World"
#print(x.upper()) #whole string uppercase .lower also a thing
#print(x.split()) #splits using spaces
#print(x.split("l")) #can use a letter to split between letters. removes letters chosen as well. shows spaces

# Formatting

#print("This a string {}".format("INSERTED"))
#print("The {} {} {}".format("little","gay","kid"))
#print("The {1} {0} {2}".format("little","gay","kid"))

# Float Formatting = basically rounding up floating point numbers
result = 100.0/739.0
#print("The result was {r:1.3f}".format(r=result)) # in this format {r:1.3f} = the number 3 is how far you want the end result to go

