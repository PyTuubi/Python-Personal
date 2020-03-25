def squared():

    while True:

        try:
            num = int(input('Input an integer: '))
            squared2 = num*num

        except:
            print('There was an error')
            continue

        else:
            print(f'Thank you, your number squared is: {squared2}')
            break

squared()