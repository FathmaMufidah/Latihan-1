# Exercise 10-11: Favorite Number (Membaca Data)

import json
from pathlib import Path

# Menentukan path file JSON di folder TUGAS
path = Path('TUGAS/favorite_number.json')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("[Error] File favorite_number.json belum dibuat.")
else:
    # Membaca data dari format JSON
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")