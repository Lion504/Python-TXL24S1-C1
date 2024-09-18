
def class_ship(class_name):

    if class_name == 'LUX':
        return 'Upper-deck cabin with a balcony.'
    elif class_name == 'A':
        return 'Above the car deck, equipped with a window.'
    elif class_name == 'B':
        return 'Windowless cabin above the car deck.'
    elif class_name == 'C':
        return 'Windowless cabin below the car deck.'
    else:
        return 'Invalid cabin class.'

class_input = input('Enter cabin class of a cruise ship name: ').upper()
result = class_ship(class_input)

print(f'{class_input} cabin class of a cruise ship is: {result}')
