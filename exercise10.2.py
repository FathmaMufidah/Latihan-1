from pathlib import Path

# Menentukan path ke file teks di folder TUGAS
path = Path('TUGAS/learning_python.txt')

# Membaca seluruh isi file
contents = path.read_text(encoding='utf-8')

print("--- Hasil Penggantian Kata 'Python' Menjadi 'C' ---")
# Looping setiap baris dan mengganti kata 'Python' menjadi 'C'
for line in contents.splitlines():
    modified_line = line.replace('Python', 'C')
    print(modified_line)