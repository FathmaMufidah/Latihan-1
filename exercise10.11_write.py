# Exercise 10-11: Favorite Number (Menyimpan Data)

import json
from pathlib import Path

# Meminta input angka favorit dari user
number = input("Masukkan angka favorit Anda: ")

# Menentukan path file JSON di folder TUGAS
path = Path('TUGAS/favorite_number.json')

# Mengonversi dan menyimpan data ke format JSON
contents = json.dumps(number)
path.write_text(contents, encoding='utf-8')

print("Angka favorit Anda telah berhasil disimpan!")