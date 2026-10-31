responses = {}

# Set flag untuk mengontrol perulangan polling
polling_active = True

while polling_active:
    # Meminta nama dan tempat impian pengguna
    name = input("\nSiapa nama Anda? ")
    response = input("Jika Anda bisa mengunjungi satu tempat di dunia, Anda ingin pergi ke mana? ")
    
    # Simpan jawaban ke dalam dictionary
    responses[name] = response
    
    # Cari tahu apakah ada orang lain yang ingin ikut polling
    repeat = input("Apakah ada orang lain yang ingin merespons? (ketik 'yes'/'no') ")
    if repeat == 'no':
        polling_active = False

# Polling selesai, tampilkan hasil
print("\n--- Hasil Jajak Pendapat Liburan Impian ---")
for name, place in responses.items():
    print(f"{name.title()} ingin sekali berkunjung ke {place.title()}.")