import sys
print(sys.stdin)

kokonimi = "Jonni Liljamo"
etunimi = "Jonni"
sukunimi = "Liljamo"
#print(etunimi + sukunimi)             # = JonniLiljamo
#print(etunimi + " " + sukunimi)        # = Jonni Liljamo           !!!!!

merkki = "^"
merkit = merkki * 10
#print(merkit)                          # = ^^^^^^^^^^

ika = 14
mjono = "Ikä on"
#print(mjono, ika, "vuotta.")           # = Ikä on 14 vuotta.

gsletters = "Jonni"
gsl1 = gsletters[1]
gsl2 = gsletters[3] + gsletters[4]
#print(gsletters[0])                    # 0 to last number = J
#print(gsl1)                            # = o
#print(gsl2)                            # = ni

#print (len("Jonni"))                   # use of len() = 5
#print (len(gsl2))                      # = 2

eka = gsletters[0]
vika = gsletters[len(gsletters) - 1]
#print(eka, vika)                       #first and last letters of a string

pituus = len("ab" + "de")
#print(pituus * 2)                      # = 8

gml = "Jonni"
#print(gml[1:3])                        # first number wanted:number after the last one that you wanted = on
#print(gml.find("on"))                  # use of .find() = 1 = "on" starts on letter number 1
#print(gml.find("ni"))                  # = 3 = "ni" starts on letter 3
#print(gml.find("yeet"))                # = -1 because gml doesnt have that str part

#.replace
rmosl = "Jonni"
#print(rmosl.replace("Jo","Je"))        # replaces Jo with Je and prints Jenni
wrp = "ala"
#print(wrp.replace("a","oma"))          # replaces both a's with oma = omaloma
kor = "J"
rmosl2 = rmosl.replace(kor," ")
#print(rmosl2)                          # = " onni" = replaces J with a space " "

#ika2 = input("Kuinka vanha olet?")
#print("Olet siis",ika2,"vuotta.")      # = Olet siis x vuotta. 
#name = input("Anna nimesi: ")
#print("Terve, " + name +"!")           # = Terve, x!   ~//~

num1 = eval(input("Anna luku 1: "))
num2 = eval(input("Anna luku 2: "))
print("Lukujen keskiarvo: ")
print((num1 + num2) / 2.0)

#nimi = input("Anna koko nimesi: ")
#print("Nimessäsi on", len(nimi), "merkkiä.")   # = number of characters
#print("Etunimesi on ",nimi[0:nimi.find(" ")])  # prints only first name, nimi[0:nimi.find(" ")] = Jonni Liljamo[start from letter 0:find and end at first space(" ")]

input("Press something to exit")           # Use when running in CMD, PowerShell or Terminal