def city_country(city, country):
    """Mengembalikan string dengan format 'City, Country'."""
    formatted_location = f"{city.title()}, {country.title()}"
    return formatted_location

# Memanggil fungsi untuk tiga pasangan kota dan negara, lalu cetak hasilnya
city1 = city_country('jakarta', 'indonesia')
print(city1)

city2 = city_country('tokyo', 'japan')
print(city2)

city3 = city_country('paris', 'france')
print(city3)