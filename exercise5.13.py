# Simulasi sistem tiket bioskop sederhana berdasarkan usia pengunjung
umur_penonton = 20

if umur_penonton < 5:
    print("Tiket gratis untuk balita!")
elif umur_penonton < 12:
    print("Harga tiket anak-anak adalah Rp25.000.")
elif umur_penonton < 60:
    print("Harga tiket dewasa adalah Rp50.000.")
else:
    print("Harga tiket lansia adalah Rp30.000.")