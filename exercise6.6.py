# Daftar orang yang sudah mengisi polling bahasa pemrograman favorit
favorite_languages = {
    'budi': 'python',
    'siti': 'java',
    'joko': 'c',
    'dewi': 'python',
}

# Daftar orang yang akan diajak/dicek status pollingnya
poll_people = ['budi', 'rudi', 'siti', 'ari', 'joko']

for person in poll_people:
    if person in favorite_languages.keys():
        print(f"Terima kasih {person.title()}, sudah meluangkan waktu mengikuti polling!")
    else:
        print(f"Halo {person.title()}, kami mengundangmu untuk mengikuti polling bahasa pemrograman.")