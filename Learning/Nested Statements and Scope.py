x = 25

def printer():
    x = 50
    return x

print(x) # 25
print(printer()) # 50

# Should be quite self explanatory

# LOCAL

# Num is local to the lambda function
lambda num: num ** 2

# GLOBAL
name = 'Jyn'

def greet():

    # ENCLOSING
    name = 'Rey'

    def hello():

        #LOCAL
        name = 'Raven'

        print('Hello ' + name)

    hello()

print(greet())


# BUILT-IN
len()
print()

# etc