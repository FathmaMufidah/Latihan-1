# Exercise 10-13: User Dictionary

import json
from pathlib import Path

path = Path('TUGAS/user_info.json')

if path.exists():
    # Jika file sudah ada, baca dan tampilkan datanya
    contents = path.read_text(encoding='utf-8')
    user_data = json.loads(contents)
    
    print("=== Ringkasan Data Pengguna ===")
    print(f"Nama    : {user_data['username']}")
    print(f"Usia    : {user_data['age']} tahun")
    print(f"Kota    : {user_data['location']}")
    print("\nSelamat datang kembali, kami masih mengingat data Anda!")
else:
    # Jika file belum ada, minta masukan data baru
    print("=== Pendaftaran Data Pengguna ===")
    username = input("Masukkan nama Anda     : ")
    age = input("Masukkan usia Anda     : ")
    location = input("Masukkan kota asal Anda: ")

    user_data = {
        'username': username,
        'age': age,
        'location': location
    }

    contents = json.dumps(user_data, indent=4)
    path.write_text(contents, encoding='utf-8')
    print("\nData Anda telah berhasil disimpan!")