def make_shirt(size='large', text='I love teknik'):
    """Menampilkan ringkasan ukuran dan teks pada kaos dengan nilai default."""
    print(f"\nMembuat kaos ukuran {size.upper()} dengan tulisan: '{text}'")

# 1. Membuat kaos ukuran Large dengan pesan default
make_shirt()

# 2. Membuat kaos ukuran Medium dengan pesan default
make_shirt(size='medium')

# 3. Membuat kaos ukuran Small dengan pesan teks yang berbeda
make_shirt(size='small', text='Senyum itu ibadah')