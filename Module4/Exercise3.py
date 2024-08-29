#Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

number = []

while True:
    input_num = input("Enter a number: ")
    if input_num == '':
        break
    elif input_num.isdigit():
        number.append(input_num)
    else:
        print("Invalid input,try again.")
if number:
    number_s = min(number)
    print(f'The smallest number is: {number_s}')
    number_l = max(number)
    print(f'The largest number is: {number_l}')

