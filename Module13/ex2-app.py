import os
from flask import Flask, jsonify
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

#fetch airport
def get_airport(icao):
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST','127.0.0.1'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
        )
        cursor = connection.cursor()
        print(f"Querying ICAO: {icao}")

        #query
        query = "SELECT ident, name, municipality FROM airports WHERE UPPER(ident) = %s"
        cursor.execute(query, (icao,))
        row = cursor.fetchone()
        connection.close()

        if row:
            return {
                "ICAO" : row[0],
                "NAME" : row[1],
                "STATUS" : row[2],
            }
        else:
            return None
    except mysql.connector.Error as error :
        print(f"{error}")
        return None

# define endpoint
@app.route('/airport/<icao>', methods=['GET'])
def show_airport(icao):
    airport = get_airport(icao)
    if airport:
        return jsonify(airport)
    else:
        return jsonify({"error": "airport no found"}),404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)