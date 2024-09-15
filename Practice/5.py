'''while True:
    user_input = int(input('Entre a number: '))
    if user_input > 1:
        for i in range(1, user_input +1) :
            if  user_input != 1 and i != user_input and user_input % i == 0:
                print(f'{user_input}It is not a prime number')
            else:
                print(f'{user_input}it is a prime number')
    else:
        print(f'{user_input}it is a prime number')
    break'''

while True:
    user_input = int(input('Entre a number: '))
    if user_input > 1:
        for i in range(1, user_input +1) :
            if  user_input != 1 and i != user_input and user_input % i == 0:
                print(f'{user_input} is not a prime number')
            else:
                print(f'{user_input} is a prime number')
    else:
        print(f'{user_input} is a prime number')
    break