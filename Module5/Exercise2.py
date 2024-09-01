#Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

# set an empty list
number = []

#repeat input number
while True:
    user_input = input("Enter a number/ Press enter to quite: ")

# empty string to quite
    if user_input == '':
        break

#set input is integer and store in number
    user_input = int(user_input)
    number.append(user_input)

#manage list as descending order and choose first 5 number
number.sort(reverse=True)
number_l = number[:5]
print(f'The 5 greatest number is: {number_l}')