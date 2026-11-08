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


class Admin(User):
    """Mewakili pengguna khusus dengan hak akses administrator."""

    def __init__(self, first_name, last_name, age, location):
        """Inisialisasi atribut dari parent class dan privileges admin."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify user settings"
        ]

    def show_privileges(self):
        """Menampilkan daftar hak akses yang dimiliki admin."""
        print(f"\nHak akses administrator untuk {self.first_name.title()} {self.last_name.title()}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Membuat instance dari class Admin
admin_user = Admin('zahrah', 'cintani', 18, 'jakarta')

# Memanggil method dari Parent Class (User)
admin_user.describe_user()

# Memanggil method dari Child Class (Admin)
admin_user.show_privileges()