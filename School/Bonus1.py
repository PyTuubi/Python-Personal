# Jonni Liljamo
# Bonus 1

import cmath


x1 = int(input("X1: "))
y1 = int(input("Y1: "))

x2 = int(input("X2: "))
y2 = int(input("Y2: "))

bSqrt = (x2 - x1) ** 2 + (y2 - y1) ** 2

pituus = cmath.sqrt(bSqrt)

print("Pituus on: " + str(pituus.real))

