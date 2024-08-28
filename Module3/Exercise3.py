'''Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.
A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l.'''

bio_g = input('Enter the biological gender (male/female): ')
hemo_v = int(input('Enter the hemoglobin value: '))

if bio_g == 'female':
    if hemo_v <117:
        print('Attention! Your hemoglobin value is low!')
    elif hemo_v >155:
        print('Attention! Your hemoglobin value is high!')
    else:
        print('Great! Your hemoglobin value is normal!')
else :
    if hemo_v < 134:
        print('Attention! Your hemoglobin value is low!')
    elif hemo_v > 167:
        print('Attention! Your hemoglobin value is high!')
    else:
        print('Great! Your hemoglobin value is normal!')