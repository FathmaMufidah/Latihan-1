from random import choice

# 1. Membuat list berisi 10 angka dan 5 huruf
lottery_pool = [1, 3, 7, 12, 15, 22, 28, 33, 40, 45, 'A', 'B', 'K', 'M', 'R']

# 2. Mengambil 4 elemen acak secara unik untuk tiket pemenang
winning_ticket = []
while len(winning_ticket) < 4:
    selected_item = choice(lottery_pool)
    if selected_item not in winning_ticket:
        winning_ticket.append(selected_item)

# 3. Mencetak pesan pemenang
print("--- Pengundian Lotere ---")
print(f"Setiap tiket yang cocok dengan 4 angka/huruf ini mendapatkan hadiah:")
print(f"-> {winning_ticket}")