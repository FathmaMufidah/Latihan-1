# exercise11_3_employee.py

class Employee:
    """Class untuk merepresentasikan seorang karyawan."""

    def __init__(self, first_name, last_name, annual_salary):
        """Menyimpan atribut nama depan, nama belakang, dan gaji tahunan."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Menambahkan gaji tahunan (default $5,000)."""
        self.annual_salary += amount