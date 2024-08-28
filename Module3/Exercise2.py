'''Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.
LUX: upper-deck cabin with a balcony.
A: above the car deck, equipped with a window.
B: windowless cabin above the car deck.
C: windowless cabin below the car deck.'''

carbin_class = input('Enter the cabin class of a cruise ship: ')

if carbin_class == 'LUX':
    print('LUX: upper-deck cabin with a balcony.')
elif carbin_class == 'A':
    print('A: above the car deck, equipped with a window.')
elif carbin_class == 'B':
    print('B: windowless cabin above the car deck.')
else:
    print('C: windowless cabin below the car deck.')