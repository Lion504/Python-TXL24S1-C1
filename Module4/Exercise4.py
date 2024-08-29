#Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

import random
number = random.randint(1,10)

while True:
    user_guess = int(input("Guess a number between 1 and 10: "))
    print(number)
    if 10 >= user_guess > number:
        print("Your guess is too high")
    elif 1 < user_guess < number:
        print("Your guess is too low")
    elif user_guess > 10 or user_guess < 1:
        print("It's invalid, number must between 1 and 10!")
    elif user_guess == number:
        print('congratulations! Your guess is correct!!!')
        user_guess = input("Next round y/n ? ")
        if user_guess == "y":
            continue
        elif user_guess == "n":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input")
            break


