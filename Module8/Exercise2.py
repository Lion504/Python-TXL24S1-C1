import mysql.connector

connection= mysql.connector.connect(
    host="localhost",
    port = '3306',
    user='root',
    password='1111',
    database='game',
    charset="utf8mb4",
    collation='utf8mb4_unicode_ci'
)
cursor = connection.cursor(dictionary=True)

def get_area (input_area):

    sql = '''SELECT airport.type, COUNT(*) AS count, 
    country.name as country_name
    FROM airport
    JOIN country ON airport.iso_country = country.iso_country
    WHERE airport.iso_country = %s 
    GROUP by country.name,airport.type
    ORDER BY airport.type'''

    try:
        cursor.execute(sql, (input_area,))
        result = cursor.fetchall()

        if result:
            airport_n = 0
            country_name = result[0]['country_name']
            type_list = []
            for row in result:
                airport_type = row['type']
                airport_count = row['count']
                type_list.append(f"{airport_count} {airport_type}")
            type_str = ', '.join(type_list)
            print(f'{country_name} has {type_str}.')

        else:
            print(f'Can not found airport in this area')
    except mysql.connector.Error as err:
        print(f'Err{err.msg}')
    finally:
        cursor.close()

input_area = input(f'Enter the area code: ').upper()
get_area(input_area)
connection.close()