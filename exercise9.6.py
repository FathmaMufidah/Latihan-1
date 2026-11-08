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


class IceCreamStand(Restaurant):
    """Mewakili restoran khusus jenis kedai es krim."""

    def __init__(self, restaurant_name, cuisine_type='es krim'):
        """Inisialisasi atribut dari parent class dan rasa es krim."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['cokelat', 'vanilla', 'stroberi', 'matcha', 'taro']

    def show_flavors(self):
        """Menampilkan daftar varian rasa es krim yang tersedia."""
        print(f"\nVarian rasa es krim yang tersedia di {self.restaurant_name.title()}:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# Membuat instance dari class IceCreamStand
my_ice_cream_shop = IceCreamStand('mixue gelato')

# Memanggil method dari Parent Class (Restaurant)
my_ice_cream_shop.describe_restaurant()

# Memanggil method dari Child Class (IceCreamStand)
my_ice_cream_shop.show_flavors()