# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

# count_primes(100) --> 25

def count_primes(n):

    # Check for 0 or 1
    if n < 2:
        return 0

    # 2 or greater

    # Store primes
    primes = [2]
    # Counter going up to input num
    x = 3

    # x is going thru every number up to input num
    while x <= n:
        # Check if x is prime
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


print(count_primes(250))