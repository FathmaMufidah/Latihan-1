def show_messages(messages):
    """Menampilkan setiap pesan teks yang ada di dalam list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Mencetak setiap pesan dan memindahkannya ke list sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

# Daftar pesan awal dan list kosong untuk menampung pesan terkirim
text_messages = [
    "Halo, apa kabar?",
    "Jangan lupa kerjain tugas Alpro ya, bestie!",
    "Sampai ketemu di kampus besok.",
    "Semangat terus ngodingnya!"
]
sent_messages = []

# Memanggil fungsi send_messages
send_messages(text_messages, sent_messages)

# Memeriksa isi kedua list setelah proses selesai
print("\n--- Status Akhir List ---")
print(f"List asli (text_messages): {text_messages}")
print(f"List terkirim (sent_messages): {sent_messages}")