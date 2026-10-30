cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': '522.700 jiwa',
        'fact': 'Dikenal sebagai Kota Budaya dan kota kelahiran Presiden Joko Widodo.',
        'landmark': 'Keraton Surakarta',
        'best_time_to_visit': 'Bulan Juli (saat ada Solo Batik Carnival)',
    },
    'tangerang': {
        'country': 'indonesia',
        'population': '1,8 juta jiwa',
        'fact': 'Kota industri dan perdagangan yang berkembang pesat di Banten.',
        'landmark': 'Masjid Al-Azhom',
        'best_time_to_visit': 'Akhir pekan (untuk wisata kuliner Pasar Lama)',
    },
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta jiwa',
        'fact': 'Salah satu kota metropolitan terbesar dan terpadat di dunia.',
        'landmark': 'Tokyo Tower',
        'best_time_to_visit': 'Musim semi (bulan Maret-Mei)',
    },
}

for city, city_info in cities.items():
    print(f"========================================")
    print(f" KOTA: {city.upper()} ")
    print(f"========================================")
    print(f"• Negara             : {city_info['country'].title()}")
    print(f"• Populasi           : {city_info['population']}")
    print(f"• Landmark           : {city_info['landmark']}")
    print(f"• Waktu Terbaik      : {city_info['best_time_to_visit']}")
    print(f"• Fakta Unik         : {city_info['fact']}")
    print(f"----------------------------------------\n")