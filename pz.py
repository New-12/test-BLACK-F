#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os

SERVER = "http://127.0.0.1:5000"  # Sunucu adresi
USER_FILE = "user.json"  # Kullanıcı bilgileri yerel dosyada tutulur

def save_user(username, password):
    with open(USER_FILE, "w") as f:
        json.dump({"username": username, "password": password}, f)

def load_user():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return None

def register():
    print("=== REGISTER ===")
    username = input("Username: ")
    password = input("Password: ")

    res = requests.post(f"{SERVER}/register", json={
        "username": username,
        "password": password
    })

    if res.ok and res.json().get("success"):
        print("[✓] Registration successful.")
        save_user(username, password)
    else:
        print("[!] Registration failed:", res.json().get("message", "Unknown error"))

def login():
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    res = requests.post(f"{SERVER}/login", json={
        "username": username,
        "password": password
    })

    if res.ok and res.json().get("success"):
        print("[✓] Login successful.")
        save_user(username, password)
    else:
        print("[!] Login failed:", res.json().get("message", "Unknown error"))

def send_message(username):
    while True:
        msg = input("Mesaj (çıkmak için 'exit'): ")
        if msg.lower() == "exit":
            break
        res = requests.post(f"{SERVER}/send", json={
            "username": username,
            "message": msg
        })
        if res.ok:
            print("[✓] Mesaj gönderildi.")
        else:
            print("[!] Mesaj gönderilemedi.")

def main():
    print("=== BLACK-F Terminal İstemcisi ===")
    user = load_user()

    if not user:
        secim = input("1: Register\n2: Login\nSeçim: ")
        if secim == "1":
            register()
        elif secim == "2":
            login()
        else:
            print("Geçersiz seçim.")
            return
        user = load_user()

    if user:
        send_message(user["username"])

if __name__ == "__main__":
    main()
