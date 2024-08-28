'''Write a program that draws two random combinations of numbers for a combination lock:
a 3-digit code where each number is between 0 and 9.
a 4-digit code where each number is between 1 and 6.'''


import random
'''
#give random range-method one
code1_1 = random.randint(0,9)
code1_2 = random.randint(0,9)
code1_3 = random.randint(0,9)
code2_1 = random.randint(1,6)
code2_2 = random.randint(1,6)
code2_3 = random.randint(1,6)
code2_4 = random.randint(1,6)

#random choose print
print(f'Suggests 3-digit random combination for combination lock is: {code1_1}{code1_2}{code1_3}')
print(f'Suggests 4-digit random combination for combination lock is: {code2_1}{code2_2}{code2_3}{code2_4}')'''

#give random range method two
code_1 = ''.join([str(random.randint(0,9))for _ in range(3)])
code_2 = ''.join([str(random.randint(1,6))for _ in range(4)])
print(f'Suggests 3-digit random combination for combination lock is: {code_1}')
print(f'Suggests 4-digit random combination for combination lock is: {code_2}')




