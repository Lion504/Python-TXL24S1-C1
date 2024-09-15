def checker(num):
    for n in range(2,int(num/2)+1):
        if num % n == 0:
            return f'{num} is not prime number'
        else:
            return f'{num} is a prime number'


while True:

    user_input = input("Enter a number: ")
    if user_input != '':
        number = checker(int(user_input))
        print(number)


