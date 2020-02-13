# Note : Pangrams are words or sentences
# containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string

def pangramCheck(s):
    
    alphabet = string.ascii_lowercase

    mySet = set()

    for l in s:
        if l in alphabet:
            mySet.add(l)

    return sorted(list(mySet)) == list(alphabet)

print(pangramCheck('The quick brown fox jumps over the lazy dog'))