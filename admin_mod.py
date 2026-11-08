"""Modul khusus untuk class Privileges dan Admin."""

# Mengimpor User dari modul user_mod.py
from user_mod import User

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