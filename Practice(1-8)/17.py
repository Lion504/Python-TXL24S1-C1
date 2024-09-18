
def calculator(convert_inche):
    convert_centimeters = convert_inche * 0.245
    return convert_centimeters

while True:
    inch_input = float(input('Enter a inches: '))
    if inch_input >=0:
        result = calculator(inch_input)
        print(f'{inch_input} inches convert to  {result: .2f} centimeters.')
    else:
        break


