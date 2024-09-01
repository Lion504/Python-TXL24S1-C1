#Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.

print('Let type 5 city names!')
city_name = []
ordinal_n = ['st','nd','rd','th','th']

for i in range(5):
    user_input = input(f'Enter {i+1}{ordinal_n[i]} city name: ')
    city_name.append(user_input)

print(f'Your input city name list:')
n = 0
for name in city_name:
    n += 1
    print(f'{n}: {name}')