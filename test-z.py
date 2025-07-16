import requests
import json
import os

SERVER_URL = "http://localhost:8080"  # Gerekirse ngrok linkiyle değiştir
username = ""
session_active = False

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def register():
    global username
    clear()
    print("=== Kayıt Ol ===")
    username = input("Kullanıcı adı: ")
    password = input("Şifre: ")

    r = requests.post(SERVER_URL + "/register", json={"username": username, "password": password})
    if r.status_code == 200:
        print("[+] Kayıt başarılı!")
    else:
        print("[-] Kayıt başarısız:", r.text)

def login():
    global username, session_active
    clear()
    print("=== Giriş Yap ===")
    username = input("Kullanıcı adı: ")
    password = input("Şifre: ")

    r = requests.post(SERVER_URL + "/login", json={"username": username, "password": password})
    if r.status_code == 200:
        print("[+] Giriş başarılı!")
        session_active = True
    else:
        print("[-] Giriş başarısız:", r.text)

def send_message():
    to = input("Kime mesaj yollanacak? ")
    msg = input("Mesaj: ")
    data = {
        "from": username,
        "to": to,
        "message": msg
    }
    r = requests.post(SERVER_URL + "/send", json=data)
    if r.status_code == 200:
        print("[+] Mesaj gönderildi.")
    else:
        print("[-] Gönderilemedi:", r.text)

def get_messages():
    r = requests.get(SERVER_URL + f"/messages?user={username}")
    if r.status_code == 200:
        messages = r.json()
        print("\n--- Mesajlar ---")
        for msg in messages:
            print(f"{msg['from']} → {msg['to']}: {msg['message']}")
    else:
        print("[-] Mesajlar alınamadı:", r.text)

def main_menu():
    while True:
        clear()
        print(f"== BLACK-F | {username} ==")
        print("1. Mesaj Gönder")
        print("2. Mesajları Gör")
        print("3. Çıkış")

        choice = input("> ")
        if choice == "1":
            send_message()
        elif choice == "2":
            get_messages()
        elif choice == "3":
            print("Çıkış yapılıyor...")
            break
        input("\nDevam etmek için enter...")

def main():
    while not session_active:
        clear()
        print("== BLACK-F'e Hoş Geldin ==")
        print("1. Giriş Yap")
        print("2. Kayıt Ol")
        print("3. Çıkış")
        choice = input("> ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            exit()
        else:
            print("Geçersiz seçim.")
            input("Devam etmek için enter...")

    main_menu()

if __name__ == "__main__":
    main()
