import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="1111",
    database="game",
    charset="utf8mb4",
    collation='utf8mb4_unicode_ci'
)

def get_icao(input_icao):
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT ident, name FROM airport WHERE ident = %s"

    try:
        cursor.execute(sql, (input_icao,))
        result = cursor.fetchall()
        if result:
            for row in result:
                print(row['name'])
        else:
            print('No result found!')
    except mysql.connector.Error as err:
        print(f'Error: {err.msg}')
    finally:
        cursor.close()

input_icao = input('Enter airport ICAO code: ').upper()
get_icao(input_icao)
connection.close()