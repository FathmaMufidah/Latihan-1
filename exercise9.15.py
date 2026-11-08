from random import choice

def generate_ticket(possibilities):
    """Menghasilkan satu tiket berisi 4 kombinasi acak."""
    ticket = []
    while len(ticket) < 4:
        selected_item = choice(possibilities)
        if selected_item not in ticket:
            ticket.append(selected_item)
    return ticket


def check_ticket(drawn_ticket, my_ticket):
    """Mengecek apakah tiket yang ditarik sama dengan tiket kita (tanpa memperdulikan urutan)."""
    return set(drawn_ticket) == set(my_ticket)


# Pool elemen lotere (10 angka & 5 huruf)
lottery_pool = [1, 3, 7, 12, 15, 22, 28, 33, 40, 45, 'A', 'B', 'K', 'M', 'R']

# Tiket pilihan kita
my_ticket = [7, 15, 'A', 'M']

plays = 0
won = False

print("Memulai simulasi pengundian lotere...")

# Perulangan sampai tiket kita menang
while not won:
    drawn_ticket = generate_ticket(lottery_pool)
    plays += 1
    won = check_ticket(drawn_ticket, my_ticket)

print("\n--- Hasil Analisis Lotere ---")
print(f"Tiket kamu                : {my_ticket}")
print(f"Jumlah pengundian dilakukan: {plays} kali")
print(f"Kamu akhirnya menang setelah {plays} kali percobaan!")