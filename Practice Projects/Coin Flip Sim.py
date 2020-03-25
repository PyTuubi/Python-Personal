import random

heads = 0
tails = 0

while True:
    ask = str(input('Flip?: '))

    flip = random.randint(0,101)

    if flip <= 49:
        heads += 1
    elif flip >= 50:
        tails += 1

    print(f'Heads: {heads} \nTails: {tails}')
