def make_shirt(size, text):
    """Menampilkan ringkasan ukuran dan teks pada kaos."""
    print(f"\nMembuat kaos ukuran {size.upper()} dengan tulisan: '{text}'")

# 1. Memanggil fungsi menggunakan Positional Arguments
make_shirt('l', 'Awali hari dengan basmalah')

# 2. Memanggil fungsi menggunakan Keyword Arguments
make_shirt(size='m', text='Jangan lupa tersenyum')