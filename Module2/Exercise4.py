#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
import math

#input
int_n1 = int(input("Enter 1st integer number: "))
int_n2 = int(input("Enter 2nd integer number: "))
int_n3 = int(input("Enter 3rd integer number: "))

#calculate
sum = int_n1 + int_n2 + int_n3
product = int_n1 * int_n2 * int_n3
average = sum / 3

#print
print(f'The sum of the numbers is:{sum}')
print(f'The product of the numbers is:{product}')
print(f'The average is:{average:.2f}')

