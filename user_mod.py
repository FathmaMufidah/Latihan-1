"""Modul khusus untuk class dasar User."""

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