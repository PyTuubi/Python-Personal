#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

#old_macdonald('macdonald') --> MacDonald

def old_macdonald(s):
    first = s[0]
    inbetween = s[1:3]
    fourth = s[3]
    rest = s[4:]

    return first.upper() + inbetween + fourth.upper() + rest

print(old_macdonald("macdonald"))
