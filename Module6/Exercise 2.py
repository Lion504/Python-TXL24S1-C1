import random

def main():
    sides = int(input("How many sides do you want?:  "))
    roll(sides)

def roll(sides_n):
    n = 0
    while n < sides_n:
        n = random.randint(1,sides_n)
        print(f'your dice is {n}')
main()