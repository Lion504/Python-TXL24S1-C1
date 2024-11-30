from flask import Flask, jsonify

app = Flask(__name__)

def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
@app.route('/numchecker/<int:num>', methods=['GET'])
def check_number(num):
    result = {
        "Number": num,
        "isPrime": prime(num)
    }
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)