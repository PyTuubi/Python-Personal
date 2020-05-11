import random
import sys

while True:
    randomnum = random.randint(0, 100)
    maxtip = 101
    mintip = 0
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
            while True:
                toohightipnum = random.randint((randomnum + 1), (randomnum + 15))
                if toohightipnum <= maxtip:
                    maxtip = toohightipnum
                    print(f"Too high. The number is under {toohightipnum}")
                    break
                elif toohightipnum > maxtip:
                    continue

        elif guess < randomnum:
            while True:
                toolowtipnum = random.randint((randomnum - 15), (randomnum - 1))
                if toolowtipnum >= mintip:
                    mintip = toolowtipnum
                    print(f"Too low. The number is more than {toolowtipnum}")
                    break
                elif toolowtipnum < mintip:
                    continue
