class User:
    """Model sederhana untuk merepresentasikan profil pengguna."""
    
    def __init__(self, first_name, last_name, age, location):
        """Inisialisasi atribut profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        
    def describe_user(self):
        """Mencetak ringkasan informasi pengguna."""
        print(f"Nama Lengkap: {self.first_name.title()} {self.last_name.title()}")
        print(f"Usia        : {self.age} tahun")
        print(f"Lokasi      : {self.location.title()}")
        
    def greet_user(self):
        """Mencetak salam personal untuk pengguna."""
        print(f"Halo, {self.first_name.title()}! Selamat datang kembali.")


# Membuat beberapa instance (objek) dari class User
user_1 = User('zahrah', 'cintani', 18, 'jakarta')
user_2 = User('naura', 'ayu', 22, 'bandung')
user_3 = User('moza', 'mazaya', 30, 'tangerang')

# Memanggil method untuk User 1
print("--- Profil User 1 ---")
user_1.describe_user()
user_1.greet_user()

# Memanggil method untuk User 2
print("\n--- Profil User 2 ---")
user_2.describe_user()
user_2.greet_user()

# Memanggil method untuk User 3
print("\n--- Profil User 3 ---")
user_3.describe_user()
user_3.greet_user()