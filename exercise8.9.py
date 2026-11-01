def show_messages(messages):
    """Menampilkan setiap pesan teks yang ada di dalam list."""
    for message in messages:
        print(message)

# Membuat list berisi beberapa pesan singkat
text_messages = [
    "Halo, apa kabar?",
    "Jangan lupa kerjain tugas Alpro ya, bestie!",
    "Sampai ketemu di kampus besok.",
    "Semangat terus ngodingnya!"
]

# Memanggil fungsi dan mengirimkan list pesan
show_messages(text_messages)