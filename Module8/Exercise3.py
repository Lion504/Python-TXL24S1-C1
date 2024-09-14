import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='1111',
    database='game',
    charset="utf8mb4",
    collation='utf8mb4_unicode_ci'
)
cursor = connection.cursor(dictionary=True)

def main(input_1,input_2):
    sql = ('''
            SELECT
            airport.latitude_deg, airport.longitude_deg, airport.ident, airport.name
            FROM airport
            WHERE airport.ident in (%s, %s)
        ''')

    cursor.execute(sql, (input_1,input_2))
    get_icao = cursor.fetchall()
    cursor.close()
    if get_icao:
        return get_icao
    else:
        print('Can not found icao')
        return None

def get_distance (airport_1, airport_2):

    lat1 = airport_1['latitude_deg']
    lon1 = airport_1['longitude_deg']
    lat2 = airport_2['latitude_deg']
    lon2 = airport_2['longitude_deg']
    distance = calculator(lat1,lon1,lat2,lon2)
    print(f'The distance between {airport_1["name"]} and {airport_2["name"]} is: {distance: .2f} Km.')

def calculator(lat1,lon1,lat2,lon2):
    airport_1_coords = (lat1,lon1)
    airport_2_coords = (lat2,lon2)

    distance = geodesic(airport_1_coords, airport_2_coords).kilometers
    return distance

input_1 = input('Entre 1st ICAO code: ').upper().strip()
input_2 = input('Entre 2st ICAO code: ').upper().strip()

airports = main(input_1,input_2)

if airports and len(airports) == 2:
    airport_1 = airports[0]
    airport_2 = airports[1]
    get_distance(airport_1,airport_2)
else:
    print('Invalid input')
connection.close()
