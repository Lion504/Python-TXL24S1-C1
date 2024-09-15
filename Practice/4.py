def num_type (n_list):
    e_list = []
    o_list =[]
    for i in n_list:
        if i % 2 == 0:
            o_list.append(i)
        else:
            e_list.append(i)
    return e_list, o_list


numbers_list = []

while True:
    user_input = input('Entre an integer (or press entre to quit): ')
    if user_input != '':
        numbers_list.append(int(user_input))
    else:
        break

print(f'Current number list: {numbers_list}')

'''e1_list, o1_list = num_type(numbers_list)
print(f'even list: {e1_list}')
print(f'odd list :{o1_list}')'''
result = num_type(numbers_list)
print(f'{result[0]}, {result[1]}')


