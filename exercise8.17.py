# Exercise 8-17: Styling Functions
# Program ini sudah disesuaikan dengan aturan PEP 8 (styling guidelines)


def describe_city(city, country='indonesia'):
    """Menampilkan kalimat yang menyatakan kota berada di suatu negara."""
    print(f"{city.title()} is in {country.title()}.")


def make_shirt(size='large', text='I love teknik'):
    """Menampilkan ringkasan ukuran dan teks pada kaos."""
    print(f"Membuat kaos ukuran {size.upper()} dengan tulisan: '{text}'")


# Memanggil fungsi di bagian bawah program
describe_city('jakarta')
describe_city('tokyo', 'japan')

make_shirt(size='small', text='Senyum itu ibadah')