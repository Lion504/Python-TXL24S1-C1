'''1c,2a,3a,4c,5c,6acd,7ac,8ad,9ac,10ab,11None,12continue,13append,14 0,15"key", value,'''

'''i=0
num = list()
while i<3:
    user_input = int(input('Enter a number'))
    num.append(user_input)
    i += 1

print(f'the largest number: {max(num)}')'''

'''def main():
    i = 0
    num_list = []
    
    while i<5:
        num_input=int(input('Enter a number: '))
        num_list.append(num_input)
        i += 1
    print(num_list)

    for n in num_list:
        if n % 2 == 0:
            num_list.remove(n)
    print(num_list)


main()'''
'''def calculator(l,w):
    perimeter = 2 * (l + w)
    area = l * w
    return perimeter,area

l_input = int(input('Enter a length of rectangle: '))
w_input = int(input('Enter a width of rectangle: '))
length, width = calculator(l_input,w_input)
print(f'the perimeter is:{length}, the area is:{width}')'''
'''numbers = [1, 2, 3, 4, 5]
i = 0

while i < len(numbers):
    for num in numbers:
        if num == numbers[i]:
            if num == 3:
                print(f"Breaking both loops at number {num}")
                break
        print(num)
    if numbers[i] == 3:
        break  # Break the outer while loop
    i += 1'''

'''1b,2d,3b,4a,5a,6a,7b,8b'''

