class User:
    """Model sederhana untuk merepresentasikan profil pengguna."""
    
    def __init__(self, first_name, last_name, age, location):
        """Inisialisasi atribut profil pengguna dan percobaan login."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0  # Nilai awal default 0
        
    def describe_user(self):
        """Mencetak ringkasan informasi pengguna."""
        print(f"Nama Lengkap: {self.first_name.title()} {self.last_name.title()}")
        print(f"Usia        : {self.age} tahun")
        print(f"Lokasi      : {self.location.title()}")
        
    def greet_user(self):
        """Mencetak salam personal untuk pengguna."""
        print(f"Halo, {self.first_name.title()}! Selamat datang kembali.")

    def increment_login_attempts(self):
        """Menambah jumlah percobaan login sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mengatur ulang percobaan login menjadi 0."""
        self.login_attempts = 0


# Membuat instance user baru
user_1 = User('zahrah', 'cintani', 18, 'jakarta')

# 1. Menyimulasikan beberapa kali percobaan login
print("Simulasi login...")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

# 2. Cetak nilai login_attempts setelah di-increment
print(f"Jumlah percobaan login saat ini: {user_1.login_attempts}")

# 3. Reset percobaan login
print("\nMereset percobaan login...")
user_1.reset_login_attempts()

# 4. Cetak nilai login_attempts setelah di-reset
print(f"Jumlah percobaan login setelah reset: {user_1.login_attempts}")