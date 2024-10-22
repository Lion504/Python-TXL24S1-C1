'''1d,2a,3a,4b,5d,6abd,7abc,8abc,9ac,10ad,11break,12items,13remove,14list,15range'''
'''i=0
num = []
while i < 5:
    user_input = int(input('Enter a integer number: '))
    num.append(user_input)
    i += 1
print(num)
print(f'largest number {max(num)}')
print(f'smallest number {min(num)}')'''

'''def get_int():
    i = 0
    n =[]
    while i < 5:
        num_input = int(input('Enter a integer number: '))
        n.append(num_input)
        i += 1
    print(n)

    for i in n[:]:
        if i % 2 != 0:
            n.remove(i)
    print(n)

get_int()'''

def leap_check(i):
    if i % 4 == 0 and i % 100 == 0 and i % 400 == 0:
        return'it is a leap year'
    else:
        return'it is not a leap year'

year_input = input('Enter a year: ')
result = leap_check(int(year_input))
print(result)
