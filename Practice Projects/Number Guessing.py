import random
import sys

while True:
    randomnum = random.randint(0, 100)
    print(randomnum)
    print("Start guessing!")
    guessing = True
    while guessing:
        guess = int(input("What are you thinking? "))
        if guess == randomnum:
            print("You got it!")
            replayq = str(input("Play again? y or n "))
            if replayq == "y":
                guessing = False
            else:
                sys.exit("nuts")
        elif guess > randomnum:
            print(f"Too much. The number is under {random.randint((randomnum + 1), (randomnum + 15))}")
