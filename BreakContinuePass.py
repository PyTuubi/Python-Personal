y = [1,2,3]

for x in y:
    pass            # Place holder, loop does nothing

mystring = "Jonni"

for letter in mystring:
    if letter == "J":
        #continue
        break           # Self explanatory
    print(letter)

x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1