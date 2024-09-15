import random
def get_dice(dices,times):
        for i in range(times):
            roll_list = []
            for j in range(dices):
                roll_dice = random.randint(1, 6)
                roll_list.append(roll_dice)

            print(f'{i+1} time you rolled {roll_list}')
            print(f'{sum(roll_list)}')

input_dice = int(input('How many dice you want to roll: '))
input_times = int(input('How many times you want to roll: '))
get_dice(input_dice,input_times)






