import random

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

try:
    for num in rand_num(1,10,12):
        print(num)
except:
    print('An error there was')