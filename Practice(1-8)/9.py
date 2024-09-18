list = []
while True:
    user_input = input('Enter a number: ')
    if user_input != '':
        list.append(int(user_input))
    else:
        break

list.sort(reverse=True)
print(f'5 Greatest number are: {list[:5]}')