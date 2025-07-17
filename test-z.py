import os
import json
import hashlib

DATA_FILE = "users.json"

# Şifreyi SHA256 ile hashle
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Kullanıcıları yükle
def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# Kullanıcıları kaydet
def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

# Kayıt olma
def register():
    users = load_users()
    username = input("Yeni kullanıcı adı: ").strip()
    if username in users:
        print("❌ Bu kullanıcı zaten kayıtlı.")
        return
    password = input("Yeni şifre: ").strip()
    users[username] = hash_password(password)
    save_users(users)
    print("✅ Kayıt başarıyla tamamlandı.")

# Giriş yapma
def login():
    users = load_users()
    username = input("Kullanıcı adınız: ").strip()
    password = input("Şifreniz: ").strip()
    if username in users and users[username] == hash_password(password):
        print(f"✅ Giriş başarılı. Hoş geldin, {username}!")
        return username
    else:
        print("❌ Hatalı kullanıcı adı veya şifre.")
        return None

# Ana menü
def main():
    while True:
        print("\n=== BLACK-F SİSTEMİ ===")
        print("1 - Giriş Yap")
        print("2 - Kayıt Ol")
        print("3 - Çıkış")

        choice = input("Seçim yap: ").strip()

        if choice == "1":
            user = login()
            if user:
                # Giriş başarılıysa burada sistemin ana fonksiyonu çağrılabilir
                print(f"🔐 {user} sistemde aktif!")
                break
        elif choice == "2":
            register()
        elif choice == "3":
            print("👋 Görüşmek üzere.")
            break
        else:
            print("⚠️ Geçersiz seçim. Tekrar dene.")

if __name__ == "__main__":
    main()
