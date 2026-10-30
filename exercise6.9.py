favorite_places = {'ari': ['pantai', 'gunung', 'perpustakaan'],
    'dewi': ['kafe', 'taman kota'],
    'sigro': ['museum', 'pantai', 'mall'],}

for name, places in favorite_places.items():
    print(f"Tempat favorit {name.title()} adalah:")
    for place in places:
        print(f"- {place}")
    print()