#Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

inch = int(input("Enter a inches: "))

while True:

    if inch > 0:
        centimeters = inch * 2.54
        print(centimeters)
        inch = float(input("Enter a inches: "))
    else:
        print('Invalid value, program ends!')
        break

