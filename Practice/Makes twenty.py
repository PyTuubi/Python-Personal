#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

def makes_twenty(x,y):
    if x + y == 20:
        return True
    elif x == 20 or y == 20:
        return True
    else:
        return False

print(makes_twenty(20,10))
