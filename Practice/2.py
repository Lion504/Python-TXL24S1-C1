user_gender = input('Entre the biological gender(male/female): ')
user_hemo = float(input('Entre the hemoglobin value(g/l): '))

if user_gender == 'male':
    if 134< user_hemo < 167:
        print('your hemoglobin value is normal!')
    elif user_hemo < 134:
        print('your hemoglobin value is low!')
    else:
        print('your hemoglobin value is high!')
elif user_gender == 'female':
    if user_hemo < 117:
        print('your hemoglobin value is low!')
    elif user_hemo > 155:
        print('your hemoglobin value is high!')
    else:
        print('your hemoglobin value is normal!')
