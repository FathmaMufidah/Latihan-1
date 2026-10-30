# Membuat tuple berisi 5 menu makanan
menu = ("nasi goreng", "mie ayam", "sate", "soto", "bakso")

print("Menu asli restoran:")
for makanan in menu:
    print(makanan)

# Jika baris di bawah ini di uncomment (dihapus tanda # nya),
# Pyhton akan memunculkan TypeError karena tuple tidak bisa diubah isinya:
# menu[0] = "bubur ayam"

# Restoran mengganti menu ( menimpa variabel tuple dengan nilai baru)
menu = ("nasi goreng", "mie ayam", "sate", "pecel lele", "rendang")

print("\nMenu revisi restoran:")
for makanan in menu:
    print(makanan)