from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "username": "user1", "password": "password1"},
    {"id": 2, "username": "user2", "password": "password2"}
]

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    user = next((user for user in users if user["username"] == username and user["password"] == password), None)
    if user:
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = {"id": len(users) + 1, "username": data.get("username"), "password": data.get("password")}
    users.append(new_user)
    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
