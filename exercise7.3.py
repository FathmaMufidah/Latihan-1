number = input("Masukkan sebuah angka, nanti saya beri tahu apakah kelipatan 10 atau bukan: ")
number = int(number)

if number % 10 == 0:
    print(f"\nAngka {number} adalah kelipatan 10.")
else:
    print(f"\nAngka {number} bukan kelipatan 10.")