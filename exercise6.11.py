cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': '522.700 jiwa',
        'fact': 'Dikenal sebagai Kota Budaya dan kota kelahiran Presiden Joko Widodo.',
        'landmark': 'Keraton Surakarta',
    },
    'tangerang': {
        'country': 'indonesia',
        'population': '1,8 juta jiwa',
        'fact': 'Kota industri dan perdagangan yang berkembang pesat di Banten.',
        'landmark': 'Masjid Al-Azhom',
    },
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta jiwa',
        'fact': 'Salah satu kota metropolitan terbesar dan terpadat di dunia.',
        'landmark': 'Tokyo Tower',
    },
}

for city, city_info in cities.items():
    print(f"Kota: {city.title()}")
    print(f"Negara: {city_info['country'].title()}")
    print(f"Populasi: {city_info['population']}")
    print(f"Landmark Utama: {city_info['landmark']}")
    print(f"Fakta Unik: {city_info['fact']}\n")