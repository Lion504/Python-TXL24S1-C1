
def checker(num):
    if num <= 2:
        return f'{num} is a prime number'
    else:
        for n in range(2,num):
            if num % n == 0:
                return f'{num} is not a prime number'

        return f'{num} is a prime number'

while True:
    user_input = int(input('Enter a number: '))
    if user_input == '':
        break
    else:
        number = checker(user_input)

    print(number)

'''def checker(num):
    if num <= 1:
        return f'{num} is not a prime number'
    for n in range(2, int(num ** 0.5) + 1):  # Only check up to sqrt(num)
        if num % n == 0:
            return f'{num} is not a prime number'
    return f'{num} is a prime number'

while True:
    user_input = input('Enter a number (or press enter to quit): ')
    if user_input == '':
        break
    else:
        number = checker(int(user_input))

    print(number)'''
