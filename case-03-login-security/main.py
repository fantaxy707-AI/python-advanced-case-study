import re
from datetime import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):

        if not re.match(r"^[a-zA-Z0-9]{5,}$", value):
            raise ValueError("Username harus alfanumerik dan minimal 5 karakter.")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):

        if not re.match(r"^(?=.*\d).{8,}$", value):
            raise ValueError("Password minimal 8 karakter dan wajib mengandung angka.")
        self._password = value

def audit_log(func):
    def wrapper(username, password):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            func(username, password)
            print(f"[{waktu}] AUDIT: User '{username}' mencoba login. Status: berhasil.")
        except ValueError as error:

            print(f"[{waktu}] AUDIT: User '{username}' mencoba login. Status: ditolak.")
    return wrapper

@audit_log
def proses_login(username, password):

    user_baru = User(username, password)
    print(f">> Sistem: Akses diberikan untuk {user_baru.username}.")

#================================================
# SKENARIO PENGUJIAN
#================================================
print("uji 1; login gagal akibat formta username sala (ada spasi & kurang karakter)")
proses_login("ubaid", "Password123")

print("\nUji 2: Login gagal akibat password tidak ada angka")
proses_login("ubaidillah", "passwordaja")

print("\nUji 3: Login berhasil")
proses_login("ubaidillah", "Password123")