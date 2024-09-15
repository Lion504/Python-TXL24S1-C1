
while True:
    user_input = float(input('Enter a inches: '))
    if user_input < 0:
        break
    else:
        print(f'{user_input} inches is {user_input*2.54: .2f} cm.')