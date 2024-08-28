#Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.

zander_l = float(input("Enter zander's length in centimeters: "))

if zander_l < 42:
    zander_below = 42 - zander_l
    print(f'This zander is {zander_below:.2f} centimeters below the size limit. Please release the fish back into the lake!')
else:
    print('This zander is perfect. Please keep it!')