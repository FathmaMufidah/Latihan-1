from pathlib import Path

# Meminta input nama dari user
name = input("Masukkan nama Anda: ")

# Menentukan path ke file guest.txt di folder TUGAS
path = Path('TUGAS/guest.txt')

# Menulis nama user ke dalam file
path.write_text(name, encoding='utf-8')

print(f"Terima kasih, {name}! Nama Anda telah disimpan di file guest.txt.")