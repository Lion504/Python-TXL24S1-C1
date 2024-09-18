list =[]
while True:
    user_input = input('Enter a city name: ')
    if user_input == '':
        break
    else:
        list.append(user_input)

print('You entered the following cities:')
for i in list:
    print(i)