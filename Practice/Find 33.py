# FIND 33:

# Given a list of ints,
# return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(n):

    for i in range(0,len(n)-1):
        if n[i] == 3 and n[i+1] == 3:
            return True
    
    return False



print(has_33([1, 3, 1, 3]))
