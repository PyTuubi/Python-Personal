def name_of_function():
    '''
    DOCSTRING: Information about the function
    INPUT: none
    OUTPUT: Hello
    '''
    print('Hello')

#name_of_function()     #Call function to execute

def example2(name):
    '''
    DOCSTRING: Information about the function
    INPUT: name
    OUTPUT: Hello [name]
    '''
    print('Hello ' + name)

#example2('Jonni')

#help(example2)     #This is what the information is for. Just in case someone else uses your code and wants to know what something does

# Use return instead of print() to save result in a variable
def add_function(num1,num2):
    return num1 + num2

result = add_function(1,2)

#print(result)

def say_hello(name='NAME'):     # If no input is given, prints 'Hello NAME' because without a default value for name it would print out an error
    print('Hello ' + name)

#say_hello()

# Example

# Find out if the word "Janna" is in a string

def dog_check(s):
    if 'dog' in s.lower(): # .lower makes it so it doesn't matter how 'dog' is spelled and it always finds it
        return True
    else:
        return False

# Make shorter

def dog_check2(s):
    return 'dog' in s.lower()

#print(dog_check('My dog ran away'))
#print(dog_check('Dog ran away'))


# Pig latin
'''
If word starts with a vowel, add 'ay' to end
If word does not start with a vowel, put first letter at end, then add 'ay'
word  --> ordway
apple --> appleay
'''

def pig_latin(word):
    if word[0] in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + word[0] + 'ay'

    return pig_word

print(pig_latin('word'))