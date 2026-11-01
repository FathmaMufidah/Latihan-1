def describe_city(city, country='indonesia'):
    """Menampilkan kalimat yang menyatakan kota berada di suatu negara."""
    print(f"{city.title()} is in {country.title()}.")

# Memanggil fungsi untuk tiga kota berbeda (minimal satu di luar negara default)
describe_city('jakarta')          # Menggunakan negara default (indonesia)
describe_city('solo')           # Menggunakan negara default (indonesia)
describe_city('tokyo', 'japan')     # Menggunakan negara non-default