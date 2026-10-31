sandwich_orders = ['tuna', 'pastrami', 'keju', 'ayam', 'daging sapi']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"Saya sedang membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nBerikut adalah daftar sandwich yang sudah selesai dibuat:")
for finished in finished_sandwiches:
    print(f"- Sandwich {finished}")