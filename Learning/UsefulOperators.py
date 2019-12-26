# range()

for num in range(10):       # From 0 to 10
    # print(num)            # Print up to 10 but not including 10
    pass

for num in range(3,10):     # From 3 to 10 but not including 10... 3 4 5 6 7 8 9
    # print(num)
    pass

for num in range(0,11,2):   # Start,stop,step...
    # print(num)
    pass

# enumerate

index_count = 0

for letter in "abcde":
    # print("At index {} the letter is {}".format(index_count,letter))
    # index_count += 1
    pass

# Same as above but much simpler, returns tuples
word = "abcde"

for item in enumerate(word):
    # print(item)
    pass

# zipping

mylist1 = [1,2,3]
mylist2 = ["a","b","c"]

for item in zip(mylist1,mylist2):
    # print(item)
    pass

# in

#print("x" in [1,2,3]) # False
list123 = [1,2,"x",3,4]
#print("x" in list123) # True

#print("key2" in {"key1":123,"key2":456})

# min max

mylist3 = [10,20,30,40,100]

#print(min(mylist3))        #10
#print(max(mylist3))        #100

# shuffle

from random import shuffle

mylist4 = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist4)
#print(mylist4)

# randint

from random import randint

#print(randint(0,100))       # Random number from 0 to 100

# input()

input("Enter a number: ")

