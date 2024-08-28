#Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

#input
length = float(input("Enter a length of a rectangle: "))
width = float(input("Enter a width of a rectangle: "))

#calculate
area = length * width
perimeter = 2 * (length + width)

#print
print(f'The perimeter of the rectangle is: {perimeter:.2f}')
print(f'The area of the rectangle is: {area:.2f}')
