
list =[]
while True:
    user_input = input('Enter a name: ')
    if user_input == '':
        break
    else:
        list.append(user_input)

print('Unique names entered:')
for i in list:
    print(i)