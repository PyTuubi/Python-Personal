def gen_squares(n):
    for num in range(n):
        yield num**2


for x in gen_squares(10):
    print(x)