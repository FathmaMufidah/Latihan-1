# Exercise 10-9: Silent Cats and Dogs

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(f'TUGAS/{filename}')
    
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Mengabaikan error secara senyap jika file tidak ditemukan
        pass
    else:
        print(f"=== Membaca File: {filename} ===")
        print(contents)