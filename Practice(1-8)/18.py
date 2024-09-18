import random

'''def roll_dice():
    roll_list = []
    while True:
        j = random.randint(1, 6)
        #print(j)
        roll_list.append(j)
        if j == 6:
            break
    print(roll_list)

roll_dice()'''

'''def roll_dice(i):
    roll_list = []
    while True:
        j = random.randint(1, 6)
        #print(j)
        roll_list.append(j)
        if j == i:
            break
    print(roll_list)

side_input = int(input('How many sides on the dice you want: '))
result = roll_dice(side_input)'''


num_list = []
while True:
    int_input = input('Enter a number: ')
    if int_input != '':
        num_list.append(int(int_input))
    else:
        break

print(f'original {num_list}')

for n in num_list:
    if n % 2 ==0:
        num_list.remove(n)
print(f'new {num_list}')
