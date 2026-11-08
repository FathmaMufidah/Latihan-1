"""Kumpulan class untuk mengelola pengguna dan administrator."""

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


class Privileges:
    """Class terpisah khusus untuk mengelola hak akses (privileges)."""

    def __init__(self, privileges=None):
        """Inisialisasi atribut privileges."""
        if privileges is None:
            self.privileges = [
                "can add post",
                "can delete post",
                "can ban user",
                "can modify user settings"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak akses yang dimiliki."""
        print("\nHak akses administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Mewakili pengguna khusus dengan hak akses administrator."""

    def __init__(self, first_name, last_name, age, location):
        """Inisialisasi atribut parent class dan instance Privileges."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()