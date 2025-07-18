import os
import requests
import json
import getpass
import platform
import time

SERVER_URL = "http://127.0.0.1:5000"
USER_FILE = "user.json"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wait():
    input("\nDevam etmek için enter...")

def generate_username():
    system_info = platform.node().replace(" ", "_")
    return f"blackf_{system_info.lower()}"

def load_user():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return None

def save_user(data):
    with open(USER_FILE, "w") as f:
        json.dump(data, f)

def register_user():
    username = generate_username()
    print(f"[*] Otomatik kullanıcı adınız: {username}")
    password = getpass.getpass("[?] Şifre oluştur: ")

    r = requests.post(SERVER_URL + "/register", json={"username": username, "password": password})
    if r.status_code == 200:
        print("[+] Kayıt başarılı.")
        save_user({"username": username, "password": password})
        return True
    else:
        print("[-] Kayıt başarısız:", r.text)
        return False

def login_user():
    user = load_user()
    if not user:
        print("[!] Kullanıcı bulunamadı. Önce kayıt olmalısınız.")
        return False

    r = requests.post(SERVER_URL + "/login", json=user)
    if r.status_code == 200:
        print("[+] Giriş başarılı.")
        return True
    else:
        print("[-] Giriş başarısız.")
        return False

def send_message():
    user = load_user()
    if not user:
        print("[!] Giriş yapılmadı.")
        return

    msg = input("Mesajınızı yazın: ")
    r = requests.post(SERVER_URL + "/send", json={"username": user["username"], "message": msg})
    if r.status_code == 200:
        print("[+] Mesaj gönderildi.")
    else:
        print("[-] Mesaj gönderilemedi:", r.text)

def get_messages():
    r = requests.get(SERVER_URL + "/messages")
    if r.status_code == 200:
        print("\n--- Gelen Mesajlar ---")
        for msg in r.json():
            print(f"{msg['username']} > {msg['message']}")
    else:
        print("[-] Mesajlar alınamadı:", r.text)

def main_menu():
    while True:
        clear()
        print("== BLACK-F | k ==")
        print("1. Mesaj Gönder")
        print("2. Mesajları Gör")
        print("3. Çıkış")
        choice = input("> ")

        if choice == "1":
            send_message()
        elif choice == "2":
            get_messages()
        elif choice == "3":
            print("[*] Çıkılıyor...")
            break
        else:
            print("[!] Geçersiz seçim.")

        wait()

def main():
    clear()
    print("== BLACK-F Giriş Sistemi ==\n")

    user = load_user()
    if user:
        print("[*] Kayıtlı kullanıcı bulundu:", user["username"])
        if login_user():
            main_menu()
        else:
            print("[!] Oturum açılamadı.")
    else:
        print("[!] Yeni kullanıcı kaydı başlatılıyor...")
        if register_user():
            main_menu()
        else:
            print("[!] Kayıt başarısız.")

if __name__ == "__main__":
    main()
