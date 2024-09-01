#Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

'''
import random

dice = int(input("How many dice you want to roll: "))
dice_times = 1

while dice_times<= dice:
    num = random.randint(1, 6)
    print(num)
    dice_times += 1'''

import random

#input
dice = int(input("How many dice you want to roll: "))

#to initialise dice prepare for next turn
while True:

# one roll a time
    for dice_n in range(dice):
        i = random.randint(1, 6)
        print(f'Your {dice_n+1} dice roll is:{i}')

#ask for next turn, return to for loop or break
    after_roll_q = input('Would you like to roll again? y/n: ')
    if after_roll_q == 'y':
        continue
    elif after_roll_q == 'n':
        print('Thank you for playing!')
        break

