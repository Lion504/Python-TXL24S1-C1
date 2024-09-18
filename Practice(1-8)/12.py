
def calculator(num):
    factorial_num = 1
    for n in range(1,num+1):
        factorial_num *= n
        #print(factorial_num)
    return factorial_num

while True:
    user_input = input('Enter a positive integer: ')
    if user_input == '':
        break
    else:
        number = calculator(int(user_input))
    print(number)
