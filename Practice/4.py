import math
'''def calculate_area(radius):
    area = math.pi * radius**2
    print(f'the area is {area: .2f}')
    return area
user_input = int(input('Enter a radius of a circle: '))
result = calculate_area(user_input)
print(f'{user_input} radius the area is {result}')'''

'''def compare_circles (radius_1,cost_1,radius_2,cost_2):

    def calculator(radius,cost):
        value = (math.pi * radius**2) / cost
        return value

    pizza_1 = calculator(radius_1,cost_1)
    pizza_2 = calculator(radius_2,cost_2)
    print(pizza_1, pizza_2)

    if pizza_1 > pizza_2:
        return 'Pizza_2 is good value!'
    else:
        return 'Pizza_1 is good value!'

r_1 = 5
c_1 = 20
r_2 = 7
c_2 = 30

result = compare_circles(r_1,c_1,r_2,c_2)
print(result)'''

'''def calculate_rectangle_properties(length,width):
    calculate_area = length * width
    calculate_perimeter = 2 * (length+width)
    return calculate_area, calculate_perimeter
l = 5
w = 10

area,perimeter = calculate_rectangle_properties(l,w)
print(f'area is {area}, perimeter is {perimeter}')'''

def describe_pizza(diameter, price, pizza_type="regular"):

    pizza_cost = calculator(diameter, price)

    if diameter > 15:
        pizza_type = "large"
    return pizza_cost, pizza_type

def calculator(c_diameter,c_price):
    pizza_cost = math.pi * c_diameter ** 2 / c_price
    return pizza_cost

d1 = 12
p1 = 10
d2 = 16
p2 = 14

description1 = describe_pizza(d1, p1)
print(f'{description1}')
description2 = describe_pizza(d2, p2)
print(f'{description2}')