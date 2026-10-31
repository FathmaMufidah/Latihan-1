# Daftar pesanan dengan 'pastrami' muncul beberapa kali
sandwich_orders = ['tuna', 'pastrami', 'keju', 'pastrami', 'ayam', 'daging sapi', 'pastrami']
finished_sandwiches = []

print("Perhatian: Deli sedang kehabisan pastrami hari ini!\n")

# Menggunakan while loop untuk menghapus semua kemunculan 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Memproses sisa pesanan yang ada
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"Saya sedang membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nBerikut adalah daftar sandwich yang sudah selesai dibuat:")
for finished in finished_sandwiches:
    print(f"- Sandwich {finished}")