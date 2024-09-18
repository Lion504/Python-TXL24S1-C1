'''import math
def calculator(radius,length,width):
    area = math.pi * radius ** 2
    perimeter = 2 * (length + width)
    r_area = length * width
    return area,perimeter,r_area

radius_input = float(input('Enter radius of a circle: '))
length_input = float(input('Enter a length of rectangle: '))
width_input = float(input('Enter a width of rectangle: '))
result,result_p,result_a = calculator(radius_input,length_input,width_input)
print(f'The area of the circle is: {result: .2f}')
print(f'The rectangle perimeter is: {result_p: .2f}')
print(f'The rectangle area ia: {result_a: .2f}')'''


num1_input = int(input('Enter 1st name: '))
num2_input = int(input('Enter 2nd name: '))
num3_input = int(input('Enter 3d name: '))
print(f'The sum is:{num1_input+num2_input+num3_input}')
print(f'The product is:{num1_input*num2_input*num3_input}')
print(f"The average is: {(num1_input+num2_input+num3_input)/3}")