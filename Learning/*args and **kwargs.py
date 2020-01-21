# arguments and keywordarguments

# *args allows for infinite amount of arguments instead of a fixed number like 2 (x,y) 3 (x,y,z)
def myfunc(*args):
    # 5% of total sum of numbers given
    return sum(args) * 0.05

def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find ant fruit here')


    