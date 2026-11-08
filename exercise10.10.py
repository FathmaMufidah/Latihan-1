# Exercise 10-10: Common Words

from pathlib import Path

# Menentukan path file di folder TUGAS
path = Path('TUGAS/sample_text.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("[Error] File sample_text.txt tidak ditemukan di folder TUGAS.")
else:
    # Mengubah seluruh teks menjadi huruf kecil
    lower_contents = contents.lower()

    # Menghitung kata 'the' (bisa mencakup kata seperti 'then', 'there', dll)
    count_the_all = lower_contents.count('the')

    # Menghitung kata 'the ' spesifik sebagai kata utuh (dengan spasi)
    count_the_exact = lower_contents.count('the ')

    print("=== Analisis Frekuensi Kata 'the' ===")
    print(f"Jumlah substring 'the' (termasuk inside words) : {count_the_all}")
    print(f"Jumlah kata utuh 'the ' (dengan spasi)          : {count_the_exact}")