class Restaurant:
    """Model sederhana untuk mempresentasikan sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut restaurant_name dan cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mencetak informasi ringkas tentang restoran."""
        print(f"Nama Restoran: {self.restaurant_name.title()}")
        print(f"Jenis Kuliner: {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Mencetakpesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name.title()} saat ini sedang buka!\n")

# Membuat instance (objek) dari class Restaurant
restaurant = Restaurant('padang pagi sore', 'kuliner nusantara')

# Mencetak kedua atribut secara terpisah (sesuai intruksi buku)
print(f"Mengakses atribut secara langsung:")
print(f"Nama: {restaurant.restaurant_name}")
print(f"Jenis: {restaurant.cuisine_type}\n")

print(f"Memanggil method describe_restaurant dan open_restaurant:")
# Memanggil kedua method
restaurant.describe_restaurant()
restaurant.open_restaurant()