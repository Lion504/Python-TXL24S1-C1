name = set()

while True:
    input_name = input('Entre a name: ')
    if input_name != '':
        name.add(input_name)
        print(f'Your current name are:{name}')
        continue
    else:
        break

print('Your final name list: ')
for i in name:
    print(i)