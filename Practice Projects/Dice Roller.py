import random

while True:

    if str(input("Roll? y or n: ")) == "y":
        diceOne = random.randint(1, 6)
        diceTwo = random.randint(1, 6)
        print(f"You rolled {diceOne} and {diceTwo}\n{diceOne + diceTwo} in total\n")
    else:
        break
