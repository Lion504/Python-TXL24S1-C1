airport = {
    '00AA': 'Aero B Ranch Airpot',
    'EFAA': 'Aavahelukka Airport',
    'EFET': 'Enontekio Airport',
    'EFKG': 'Kumlinge Airport',
    'EFPI': 'Piikajarvi Airport'
}

while True:
    user_input = input('Do you want entre a new airport? y/n or quit: ')
    if user_input == '':
        continue
    else:
        if user_input == 'y':
            new_icao = input('Enter new airport ICAO code: ').strip().upper()
            new_airport = input('Enter new airport name: ')
            airport[new_icao] = new_airport
        elif user_input == 'n':
                input_icao = input('Enter a airport ICAO code: ').strip().upper()
                try:
                    if input_icao in airport:
                        print(f'you are in {airport[input_icao]} now!')
                    else:
                        print('No airport available')
                except KeyError:
                    print('Please enter a valid ICAO code')
        elif user_input == 'quit':
            print('GoodBye!')
            break
