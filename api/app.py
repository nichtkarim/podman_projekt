from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_user():
    conn = sqlite3.connect('/db/users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE id=1")
    user = cursor.fetchone()
    conn.close()
    return user[0]

@app.route('/user', methods=['GET'])
def user():
    return jsonify({"name": get_user()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
