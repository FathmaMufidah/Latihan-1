while True:
    age = input("Berapa usia Anda? (Ketik 'quit' untuk keluar): ")
    
    if age == 'quit':
        break  # Langsung keluar dari loop secara paksa
    
    age_num = int(age)
    if age_num < 3:
        print("Tiket Anda gratis!\n")
    elif age_num <= 12:
        print("Harga tiket Anda adalah $10.\n")
    else:
        print("Harga tiket Anda adalah $15.\n")

print("Program selesai.")