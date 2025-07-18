import os
import requests
import json
import getpass
import platform

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

def register():
    clear()
    print("=== REGISTER ===")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()

    try:
        res = requests.post(SERVER_URL + "/register", json={"username": username, "password": password})
        print("Status code:", res.status_code)
        print("Response text:", res.text)
        if res.status_code == 200:
            print("[+] Kayıt başarılı.")
            save_user({"username": username, "password": password})
            return True
        else:
            print("[!] Kayıt başarısız:", res.json().get("error", "Bilinmeyen hata"))
            return False
    except requests.exceptions.RequestException as e:
        print("[!] Sunucuya bağlanırken hata oluştu:", e)
        return False

def login():
    clear()
    print("=== LOGIN ===")
    user = load_user()
    if not user:
        print("[!] Kayıtlı kullanıcı bulunamadı.")
        return False
    try:
        res = requests.post(SERVER_URL + "/login", json=user)
        print("Status code:", res.status_code)
        print("Response text:", res.text)
        if res.status_code == 200:
            print("[+] Giriş başarılı.")
            return True
        else:
            print("[!] Giriş başarısız:", res.json().get("error", "Bilinmeyen hata"))
            return False
    except requests.exceptions.RequestException as e:
        print("[!] Sunucuya bağlanırken hata oluştu:", e)
        return False

def send_message():
    clear()
    print("=== MESAJ GÖNDER ===")
    user = load_user()
    if not user:
        print("[!] Önce giriş yapmalısınız.")
        return
    msg = input("Mesajınız: ").strip()
    try:
        res = requests.post(SERVER_URL + "/send", json={"username": user["username"], "message": msg})
        if res.status_code == 200:
            print("[+] Mesaj gönderildi.")
        else:
            print("[!] Mesaj gönderilemedi:", res.json().get("error", "Bilinmeyen hata"))
    except requests.exceptions.RequestException as e:
        print("[!] Sunucuya bağlanırken hata oluştu:", e)

def get_messages():
    clear()
    print("=== GELEN MESAJLAR ===")
    try:
        res = requests.get(SERVER_URL + "/messages")
        if res.status_code == 200:
            messages = res.json()
            if not messages:
                print("[*] Mesaj yok.")
            for msg in messages:
                print(f"{msg['username']} > {msg['message']}")
        else:
            print("[!] Mesajlar alınamadı:", res.json().get("error", "Bilinmeyen hata"))
    except requests.exceptions.RequestException as e:
        print("[!] Sunucuya bağlanırken hata oluştu:", e)

def main_menu():
    while True:
        clear()
        print("=== BLACK-F Terminal İstemcisi ===")
        print("1: Mesaj Gönder")
        print("2: Mesajları Gör")
        print("3: Çıkış")
        choice = input("Seçim: ").strip()

        if choice == "1":
            send_message()
        elif choice == "2":
            get_messages()
        elif choice == "3":
            print("[*] Çıkış yapılıyor...")
            break
        else:
            print("[!] Geçersiz seçim.")

        wait()

def main():
    clear()
    print("=== BLACK-F Terminal İstemcisi ===")
    print("1: Register")
    print("2: Login")
    choice = input("Seçim: ").strip()

    if choice == "1":
        if register():
            main_menu()
    elif choice == "2":
        if login():
            main_menu()
    else:
        print("[!] Geçersiz seçim.")

if __name__ == "__main__":
    main()
