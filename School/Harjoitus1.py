# Jonni Liljamo
# Harjoitustyö 1

import cmath

lukuA = int(input("Luku A: "))
lukuB = int(input("Luku B: "))
lukuC = int(input("Luku C: "))

lukuD = lukuB ** 2 - 4 * lukuA * lukuC

if int(lukuD) == 0:
    V1 = (-lukuB+cmath.sqrt(lukuB**2-4*lukuA*lukuC))/2*lukuA
    print("lukuD oli 0, vastaus on: " + str(V1.real))
elif int(lukuD) > 0:
    V2 = (-lukuB+cmath.sqrt((lukuB**2)-(4*(lukuA*lukuC))))/(2*lukuA)
    V3 = (-lukuB-cmath.sqrt((lukuB**2)-(4*(lukuA*lukuC))))/(2*lukuA)
    print("lukuD oli suurempi kuin 0, vastaus on: " + str(V2.real) + " ja " + str(V3.real))   #Täytyy muuttaa complex() numerot str() muotoon että voi tulostaa samaan aikaan
                                                                                              # koska complex() numeroita ei voi muuttaa int() tai float() numeroiksi
elif int(lukuD) < 0:
    V4 = (-lukuB+cmath.sqrt(lukuB**2)-(4*(lukuA*lukuC)))/2*lukuA
    V5 = (-lukuB-cmath.sqrt(lukuB**2)-(4*(lukuA*lukuC)))/2*lukuA
    print("Ei oikeaa vastausta mutta jos silti laskee, vastaus on: " + str(V4.real) + " ja " + str(V5.real)) # x.real poistaa "+0j" osan vastauksen lopusta
else:
    print("Jotain meni pieleen")

print("lukuD oli: " + str(lukuD))

