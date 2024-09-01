'''Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.
For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.'''

'''user_input = int(input("Enter a number: "))

while user_input > 1:

    if user_input % 2 != 0 or user_input % 3 != 0:
        #if user_input % 1 == 0 and user_input % user_input == 0:
        print(f"{user_input} is a prime number.")
        #else:
            #print(f"{user_input} is not a prime number.")
        break
    else:
        print(f"{user_input} is not a prime number.")
        break
print(f"{user_input} is not a prime number.")'''

user_input = int(input("Enter a number: "))

if user_input > 1:

    for i in range(2, int(user_input ** 0.5) + 1):
        if user_input % i == 0:
            print(f"{user_input} is not a prime number.")
            break
    else:
        print(f"{user_input} is a prime number.")

else:
    print(f"{user_input} is not a prime number.")

