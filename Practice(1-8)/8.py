'''import random

def dice_roll(dice,times):
    while True:
        t = 0
        if t > times:
            break
        else:
            list = []
            for d in range(dice):
                for i in range(random.randint(1,7)):
                    list.append(i)
            print(list)
            sum = sum(list[])
            print(sum)
        return list

input_dice = int(input('how many dice you want to roll: '))
input_times = int(input('how many times you want to roll: '))
dice_roll(input_dice,input_times)'''


import random
def dice_roll(dice,times):
    for t in range(times):
        list = []
        for _ in range(dice):
            dice_rolled = random.randint(1,6)
            list.append(dice_rolled)
        print(f'your {t+1} dice roll are: {list}')
        #sum_roll = sum(list)
        print(f'the sum is {sum(list)}')

while True:
    user_dice = int(input('How many dice you want roll: '))
    user_times = int(input('How many times you want to roll: '))
    if user_dice == '' or user_times == '':
        break
    else:
        dice_roll(user_dice,user_times)