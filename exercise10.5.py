from pathlib import Path

names = []

print("=== Buku Tamu Digital ===")
print("Ketik 'quit' untuk mengakhiri program.\n")

while True:
    name = input("Masukkan nama Anda: ")
    if name.lower() == 'quit':
        break
    else:
        print(f"Selamat datang, {name.title()}!")
        names.append(name.title())

# Menggabungkan seluruh nama dengan baris baru (\n)
file_content = ""
for n in names:
    file_content += f"{n}\n"

# Menulis seluruh daftar nama ke file guest_book.txt di folder TUGAS
path = Path('TUGAS/guest_book.txt')
path.write_text(file_content, encoding='utf-8')

print("\nSeluruh nama buku tamu telah berhasil disimpan ke file guest_book.txt!")