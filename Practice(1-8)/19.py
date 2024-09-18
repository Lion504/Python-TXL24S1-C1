'''1b,2c,3d,4a,5c,6abd,7ad,8ab,9abd,10a,11area**2,12for,13def,14order,15defined'''
'''num1 = int(input('Enter a integer number: '))
num2 = int(input('Enter 2nd integer number: '))
num3 = int(input('Enter 3rd integer number: '))
print(f'sum: {num1+num2+num3}')
print(f'product: {num1*num2*num3}')
print(f'average: {(num1+num2+num3)/3}')'''
'''import random

def guess():
    n = random.randint(1,10)
    while True:
        num_guess = int(input('Guess a number: '))
        if num_guess == n:
            print('good guess!')
            break
        elif num_guess > n:
            print('too high')
        else:
            print('too low')

guess()'''

def class_cabin(i):
    if i == 'LUX':
        print(f'{i}: Upper-deck cabin with a balcony.')
    elif i == 'A':
        print(f'{i}: Above the car deck, equipped with a window.')
    elif i == 'B':
        print(f'{i}: Windowless cabin above the car deck.')
    elif i == 'C':
        print(f'{i}: Windowless cabin below the car deck.')
    else:
        print('invalid input')

while True:
    class_name = input('Enter a cabin class: ').upper()
    if class_name != '':
        result = class_cabin(class_name)
    else:
        break
