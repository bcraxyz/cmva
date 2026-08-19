import os
import sqlite3
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return jsonify(user)

@app.route('/read_file')
def read_file():
    filename = request.args.get('file')
    with open(os.path.join('/var/www/uploads', filename), 'r') as f:
        content = f.read()
    return content

@app.route('/ping')
def ping_host():
    ip = request.args.get('ip')
    cmd = f"ping -c 1 {ip}"
    os.system(cmd)
    return "Ping initiated"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == '__main__':
    app.run(debug=True)
