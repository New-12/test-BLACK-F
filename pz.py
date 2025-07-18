import requests
import json
import os
import time
import uuid

URL = "http://127.0.0.1:5000"
USER_FILE = "user_info.json"

def generate_username():
    return f"user-{uuid.uuid4().hex[:6]}"

def load_user():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return None

def save_user(user):
    with open(USER_FILE, "w") as f:
        json.dump(user, f)

def register(user):
    try:
        response = requests.post(f"{URL}/register", json=user)
        return response.status_code == 200
    except Exception as e:
        print("[-] Kayıt başarısız:", e)
        return False

def login(user):
    try:
        response = requests.post(f"{URL}/login", json=user)
        return response.status_code == 200
    except Exception as e:
        print("[-] Giriş başarısız:", e)
        return False

def send_message(user, msg):
    try:
        data = {
            "username": user["username"],
            "password": user["password"],
            "message": msg
        }
        response = requests.post(f"{URL}/send", json=data)
        return response.status_code == 200
    except Exception as e:
        print("[-] Mesaj gönderilemedi:", e)
        return False

def get_messages(user):
    try:
        data = {
            "username": user["username"],
            "password": user["password"]
        }
        response = requests.post(f"{URL}/messages", json=data)
        if response.status_code == 200:
            return response.json().get("messages", [])
        else:
            print("[-] Sunucu mesajları vermedi.")
    except Exception as e:
        print("[-] Mesajlar alınamadı:", e)
    return []

def wait():
    input("\nDevam etmek için enter...")

def main_menu(user):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("== BLACK-F | k ==")
        print("1. Mesaj Gönder")
        print("2. Mesajları Gör")
        print("3. Çıkış")
        choice = input("> ")

        if choice == "1":
            msg = input("Mesajınız: ")
            if send_message(user, msg):
                print("[+] Mesaj gönderildi.")
            else:
                print("[-] Mesaj gönderilemedi.")
            wait()

        elif choice == "2":
            messages = get_messages(user)
            print("\n== Gelen Mesajlar ==")
            if messages:
                for m in messages:
                    print(f"- {m}")
            else:
                print("[!] Hiç mesaj yok.")
            wait()

        elif choice == "3":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim.")
            wait()

if __name__ == "__main__":
    user = load_user()
    if not user:
        # İlk kez çalıştırılıyorsa kullanıcı oluştur
        username = generate_username()
        password = uuid.uuid4().hex[:8]
        user = {"username": username, "password": password}
        if register(user):
            save_user(user)
            print(f"[+] Yeni kullanıcı kaydedildi: {username}")
        else:
            print("[-] Kayıt başarısız.")
            exit()

    if login(user):
        main_menu(user)
    else:
        print("[-] Giriş başarısız. Kayıtlı bilgileri silmek için 'user_info.json' dosyasını silin.")
