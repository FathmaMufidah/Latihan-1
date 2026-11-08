# Exercise 10-6: Addition

print("=== Penjumlahan Dua Angka ===")

try:
    first_number = input("Masukkan angka pertama: ")
    num1 = int(first_number)

    second_number = input("Masukkan angka kedua  : ")
    num2 = int(second_number)
except ValueError:
    print("\n[Error] Harap masukkan angka yang valid, bukan teks!")
else:
    total = num1 + num2
    print(f"\nHasil penjumlahan {num1} + {num2} adalah: {total}")