class Restaurant:
    """Model sederhana untuk merepresentasikan sebuah restoran."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut restaurant_name, cuisine_type, dan number_served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Nilai default 0
        
    def describe_restaurant(self):
        """Mencetak informasi ringkas tentang restoran."""
        print(f"Nama Restoran: {self.restaurant_name.title()}")
        print(f"Jenis Kuliner: {self.cuisine_type.title()}")
        
    def open_restaurant(self):
        """Mencetak pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name.title()} saat ini sedang buka!")

    def set_number_served(self, number):
        """Menetapkan jumlah pelanggan yang telah dilayani."""
        self.number_served = number

    def increment_number_served(self, additional_served):
        """Menambahkan jumlah pelanggan yang telah dilayani."""
        self.number_served += additional_served


# Membuat instance restoran
restaurant = Restaurant('sate padang ajo', 'kuliner nusantara')

# 1. Cetak jumlah pelanggan awal (default)
print(f"Jumlah pelanggan terlayani (awal): {restaurant.number_served}")

# 2. Mengubah nilai atribut secara langsung
restaurant.number_served = 15
print(f"Jumlah pelanggan terlayani (setelah diubah langsung): {restaurant.number_served}")

# 3. Menggunakan method set_number_served()
restaurant.set_number_served(45)
print(f"Jumlah pelanggan terlayani (menggunakan set_number_served): {restaurant.number_served}")

# 4. Menggunakan method increment_number_served()
restaurant.increment_number_served(30)
print(f"Jumlah pelanggan terlayani (setelah increment): {restaurant.number_served}")