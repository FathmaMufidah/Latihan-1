import math
from random import shuffle

print("=== Eksplorasi Modul Standard Python ===")

# 1. Eksplorasi modul random: shuffle()
dek_kartu = ['King', 'Queen', 'Jack', 'Ace', 10]
print(f"Kartu sebelum diacak : {dek_kartu}")

shuffle(dek_kartu)
print(f"Kartu setelah diacak : {dek_kartu}\n")

# 2. Eksplorasi modul math: sqrt() dan pi
angka = 144
akar_angka = math.sqrt(angka)
print(f"Akar kuadrat dari {angka} adalah: {akar_angka}")
print(f"Nilai Pi hingga 4 desimal   : {math.pi:.4f}")