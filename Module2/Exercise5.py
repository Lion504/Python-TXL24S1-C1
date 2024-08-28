'''Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
One talent is 20 pounds.
One pound is 32 lots.
One lot is 13,3 grams.'''

#input
mass_t = float(input("Enter a mass in talents(leiviskä): "))
mass_p = float(input("Enter a mass in pounds(naula): "))
mass_l = float(input("Enter a mass in lots(luoti): "))

#calculate mass_t print
mass_t_gram = mass_t * 20 * 32 * 13.3
mass_t_kilogram = mass_t_gram * 0.001
print(f'{mass_t} talents(leiviskä) = {mass_t_gram:.2f} grams and {mass_t_kilogram:.2f} kilograms.')

#calculate mass_p print
mass_p_gram = mass_p * 32 * 13.3
mass_p_kilogram = mass_p_gram * 0.001
print(f'{mass_p} pounds(naula) = {mass_p_gram:.2f} grams and {mass_p_kilogram:.2f} kilograms. ')

#calculate mass_l print
mass_l_gram = mass_l * 13.3
mass_l_kilogram = mass_l_gram * 0.001
print(f'{mass_l} lots(luoti) = {mass_l_gram:.2f} grams and {mass_l_kilogram:.2f} kilograms. ')




