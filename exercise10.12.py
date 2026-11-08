import json
from pathlib import Path

path = Path('TUGAS/favorite_number.json')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    # Jika file belum ada, minta input dan simpan
    number = input("Masukkan angka favorit Anda: ")
    contents = json.dumps(number)
    path.write_text(contents, encoding='utf-8')
    print("Angka favorit Anda telah berhasil disimpan!")
else:
    # Jika file sudah ada, tampilkan angkanya
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")