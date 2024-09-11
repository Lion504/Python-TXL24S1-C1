def main():
        gasoline = user_input()
        convert(gasoline)

def convert(gas):
    if gas is not None:
        liter = gas * 3.785412
        print(f'{gas} Gallons = {liter: .2f} Litres')

def user_input():
    while True:
        try:
            user_input = int(input("Entre a Gasoline Volume:  "))
            if user_input >= 0:
                return user_input
            else:
                break
        except ValueError:
            print(f'Invalid value!')
main()