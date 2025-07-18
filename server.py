from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

USERS_FILE = "users.json"
MESSAGES_FILE = "messages.json"

def load_json(file):
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)
    with open(file, "r") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    users = load_json(USERS_FILE)
    if any(u["username"] == username for u in users):
        return jsonify({"error": "Kullanıcı zaten var."}), 400

    users.append({"username": username, "password": password})
    save_json(USERS_FILE, users)
    return jsonify({"message": "Kayıt başarılı."}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    users = load_json(USERS_FILE)
    if any(u["username"] == username and u["password"] == password for u in users):
        return jsonify({"message": "Giriş başarılı."}), 200
    return jsonify({"error": "Geçersiz kullanıcı adı veya şifre."}), 401

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    username = data.get("username")
    message = data.get("message")

    messages = load_json(MESSAGES_FILE)
    messages.append({"username": username, "message": message})
    save_json(MESSAGES_FILE, messages)
    return jsonify({"message": "Mesaj kaydedildi."}), 200

@app.route("/messages", methods=["GET"])
def messages():
    return jsonify(load_json(MESSAGES_FILE)), 200

if __name__ == "__main__":
    app.run(debug=True)
