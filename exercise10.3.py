from pathlib import Path

# Menentukan path ke file teks
path = Path('TUGAS/learning_python.txt')

# Membaca isi file langsung tanpa variabel sementara untuk list baris
print("--- Membaca File dengan Kode Lebih Ringkas ---")
for line in path.read_text(encoding='utf-8').splitlines():
    print(line)