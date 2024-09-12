import math
def main():
    input_diameter1,input_price1,input_diameter2,input_price2 = get_input()
    p_value1, p_value2 = p_calculate(input_diameter1,input_price1,input_diameter2,input_price2)
    value_best = p_compare(p_value1, p_value2)
    if value_best == p_value1:
        print(f'pizza 1 is best value for money.')
    else:
        print(f'pizza 2 is best value for money.')

def get_input():
    input_diameter1 = float(input('Entre a diameter of the pizza 1 in centimeter: '))
    input_price1 = float(input('Entre a price of the pizza 1 in Euros: '))
    input_diameter2 = float(input('Entre a diameter of the pizza 2 in centimeter: '))
    input_price2 = float(input('Entre a price of the pizza 2 in Euros: '))
    return input_diameter1, input_price1, input_diameter2, input_price2

def p_calculate(input_diameter1, input_price1, input_diameter2, input_price2):
    dia1 = input_diameter1 / 100
    dia2 = input_diameter2 / 100
    p_area1 = ((dia1 / 2) ** 2) * math.pi
    p_area2 = ((dia2 / 2) ** 2) * math.pi
    p_value1 = p_area1 / input_price1
    p_value2 = p_area2 / input_price2
    return p_value1, p_value2

def p_compare(p_value1, p_value2):

    if p_value1 > p_value2:
        return p_value1
    else:
        return p_value2

main()