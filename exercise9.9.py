class Car:
    """Model sederhana untuk merepresentasikan sebuah mobil."""

    def __init__(self, make, model, year):
        """Inisialisasi atribut merk, model, dan tahun."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Mengembalikan nama deskriptif yang rapi."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:
    """Model sederhana untuk baterai mobil listrik."""

    def __init__(self, battery_size=40):
        """Inisialisasi atribut ukuran baterai (default 40 kWh)."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Mencetak informasi kapasitas baterai."""
        print(f"Mobil ini memiliki kapasitas baterai {self.battery_size}-kWh.")

    def get_range(self):
        """Mencetak perkiraan jarak tempuh berdasarkan kapasitas baterai."""
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225

        print(f"Mobil ini dapat menempuh jarak sekitar {range_miles} mil dengan baterai penuh.")

    def upgrade_battery(self):
        """Mengecek dan memperbarui kapasitas baterai menjadi 65 kWh jika belum 65."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("\nBaterai berhasil di-upgrade ke 65 kWh!")
        else:
            print("\nBaterai sudah berada pada kapasitas maksimum (65 kWh).")


class ElectricCar(Car):
    """Mewakili mobil listrik yang merupakan turunan dari class Car."""

    def __init__(self, make, model, year):
        """Inisialisasi atribut parent class dan atribut spesifik mobil listrik."""
        super().__init__(make, model, year)
        self.battery = Battery()


# Membuat instance dari ElectricCar
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Cetak informasi awal mobil dan jarak tempuh (baterai default 40 kWh)
print(f"Mobil: {my_leaf.get_descriptive_name()}")
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

# Upgrade baterai
my_leaf.battery.upgrade_battery()

# Cek kembali kapasitas baterai dan jarak tempuh setelah upgrade
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()