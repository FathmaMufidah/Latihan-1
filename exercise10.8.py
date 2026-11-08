from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(f'TUGAS/{filename}')

    print(f"\n=== Membaca File: {filename} ===")
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"[Error] Maaf, file '{filename}' tidak ditemukan di folder TUGAS.")
    else:
        print(contents)