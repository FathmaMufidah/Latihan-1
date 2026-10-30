favorite_numbers = {'ari': [7, 14],
    'budi': [12, 5, 8],
    'siti': [3],
    'joko': [9, 99],
    'dewi': [1, 2, 3],}

for name, numbers in favorite_numbers.items():
    print(f"Angka favorit {name.title()} adalah:")
    for number in numbers:
        print(f"- {number}")
    print()