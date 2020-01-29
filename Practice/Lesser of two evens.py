# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(x,y):
    if x % 2 == 0 and y % 2 == 0:
        if x < y:
            print(x)
        elif x > y:
            print(y)
    elif x % 2 != 0 or y % 2 != 0:
        if x < y:
            print(y)
        elif x > y:
            print(x)
        
lesser_of_two_evens(2,4)
