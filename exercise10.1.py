from pathlib import Path

# Menentukan path ke file teks
path = Path('TUGAS/learning_python.txt')

# Reading 1: Membaca seluruh isi file sekaligus
print("--- 1. Membaca Seluruh Isi File Sekaligus ---")
contents = path.read_text()
print(contents)

# Reading 2: Menyimpan baris ke dalam list lalu looping
print("--- 2. Looping Melalui Baris yang Disimpan dalam List ---")
lines = contents.splitlines()

for line in lines:
    print(line)