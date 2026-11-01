def make_album(artist_name, album_title, tracks=None):
    """Membangun dictionary yang mendeskripsikan sebuah album musik."""
    album_dict = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    
    if tracks:
        album_dict['tracks'] = tracks
        
    return album_dict

print("Masukkan informasi album musik.")
print("(Ketik 'quit' kapan saja untuk keluar)\n")

# Menggunakan while loop agar program bisa menerima input berulang kali
while True:
    artist = input("Nama artis: ")
    if artist == 'quit':
        break
        
    title = input("Judul album: ")
    if title == 'quit':
        break
        
    # Panggil fungsi make_album dan cetak dictionary yang dihasilkan
    album = make_album(artist, title)
    print("\nDictionary album yang dibuat:")
    print(album)
    print("-" * 40)

print("\nProgram selesai. Terima kasih!")