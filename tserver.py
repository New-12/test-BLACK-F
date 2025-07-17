from flask import Flask, request, jsonify
import hashlib
import json
import os

app = Flask(__name__)
USER_FILE = "users.json"

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    users = load_users()
    username = data["username"]
    password = hash_password(data["password"])
    if users.get(username) == password:
        return jsonify({"status": "success"})
    return jsonify({"status": "fail"}), 401

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    users = load_users()
    username = data["username"]
    if username in users:
        return jsonify({"status": "exists"}), 409
    users[username] = hash_password(data["password"])
    save_users(users)
    return jsonify({"status": "registered"})

if __name__ == "__main__":
    app.run(port=8080)
