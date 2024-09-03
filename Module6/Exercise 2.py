#Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.
import random
def main():
    user_input = int(input("Enter a number of sides: "))
    t = roll(user_input)
    print(f'Wow! You just used {t} times, congratulations! ')

def roll(user_input):
    r = 0
    times = 0
    while r != user_input:
        r = random.randint(1, user_input)
        times += 1
        print(f'You rolled {r}.')
    return times

main()