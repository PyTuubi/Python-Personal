import random


v = "sininen punainen vihrea musta valkoinen oranssi purppura keltainen"
v += " harmaa ruskea"
vlista = v.split()

e = "kettu karhu kani koira kissa hirvi leijona peura seepra kirahvi "
e += "perhonen ampiainen lammas hyttynen kirppu kotka haukka"
elista = e.split()

sanapari = random.choice(vlista) + " " + random.choice(elista)

print("Sanapari:" + sanapari)

eka = sanapari.split(' ', 1)[0]

print("Eka sana:", eka.strip())

# https://stackoverflow.com/questions/13750265/how-to-get-the-first-word-in-the-string
