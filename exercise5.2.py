# Tes kesetaraan dan ketidaksetaraan dengan string
makanan = "Nasi Goreng"
print("Tes kesetaraan string:", makanan == "Nasi Goreng")
print("Tes ketidaksetaraan string:", makanan != "Bubur Ayam")

# Tes menggunakan metode lower()
kota = "Surakarta"
print("Tes lower() True:", kota.lower() == "surakarta")
print("Tes lower() False:", kota.lower() == "jakarta")

# Tes numerik (sama dengan, tidak sama dengan, > , < , >= , <=)
umur = 18
print("Tes sama dengan:", umur == 18)
print("Tes tidak sama dengan:", umur != 20)
print("Tes lebih besar:", umur > 21)
print("Tes kurang dari:", umur < 25)
print("Tes lebih besar atau sama dengan:", umur >= 18)
print("Tes kurang dari atau sama dengan:", umur <= 15)

# Tes menggunakan keyword 'and' dan 'or'
nilai_uts = 80
nilai_uas = 85
print("Tes AND (keduanya True):", nilai_uts >= 75 and nilai_uas >= 75)
print("Tes OR (salah satu True):", nilai_uts >= 90 or nilai_uas >= 80)

# Tes apakah item ada di dalam list (in) dan tidak ada di dalam list (not in)
hobi_saya = ["merajut", "membaca", "coding"]
print("Tes item ada di list (in):", "merajut" in hobi_saya)
print("Tes item tidak ada di list (not in):", "gaming" not in hobi_saya)