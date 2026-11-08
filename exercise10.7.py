# Exercise 10-7: Addition Calculator

print("=== Kalkulator Penjumlahan ===")
print("Ketik 'quit' kapan saja untuk keluar.\n")

while True:
    first_number = input("Masukkan angka pertama: ")
    if first_number.lower() == 'quit':
        break

    second_number = input("Masukkan angka kedua  : ")
    if second_number.lower() == 'quit':
        break

    try:
        num1 = int(first_number)
        num2 = int(second_number)
    except ValueError:
        print("\n[Error] Harap masukkan angka yang valid, bukan teks! Silakan coba lagi.\n")
    else:
        total = num1 + num2
        print(f"\nHasil penjumlahan {num1} + {num2} adalah: {total}\n")

print("Terima kasih telah menggunakan kalkulator!")