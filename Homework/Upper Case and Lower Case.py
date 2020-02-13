# .isupper() and .islower()

def up_low(s):

    uppers = []
    lowers = []

    for l in s:
        if l.isupper():
            uppers.append(l)
        elif l.islower():
            lowers.append(l)

    return(f'Uppercase letters: {len(uppers)} \nLowercase letters: {len(lowers)}')




print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))