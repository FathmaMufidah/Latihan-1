class Restaurant:
    """Model sederhana untuk merepresentasikan sebuah restoran."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut restaurant_name dan cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Mencetak informasi ringkas tentang restoran."""
        print(f"Nama Restoran: {self.restaurant_name.title()}")
        print(f"Jenis Kuliner: {self.cuisine_type.title()}")
        
    def open_restaurant(self):
        """Mencetak pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name.title()} saat ini sedang buka!")


# Membuat 3 instance berbeda dari class Restaurant
restaurant_1 = Restaurant('warung sunda bu las', 'masakan sunda')
restaurant_2 = Restaurant('sushi tei', 'masakan jepang')
restaurant_3 = Restaurant('pizzeria italia', 'masakan italia')

# Memanggil method describe_restaurant() untuk setiap instance
print("--- Restoran 1 ---")
restaurant_1.describe_restaurant()

print("\n--- Restoran 2 ---")
restaurant_2.describe_restaurant()

print("\n--- Restoran 3 ---")
restaurant_3.describe_restaurant()