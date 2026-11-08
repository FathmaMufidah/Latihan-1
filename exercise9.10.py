# Mengimpor class Restaurant dari modul restaurant.py
from restaurant import Restaurant

# Buat instance dari class Restaurant
my_restaurant = Restaurant('gacoan solo', 'mie pedas')

# Panggil method untuk membuktikan import berhasil
print("Testing import class Restaurant:")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()