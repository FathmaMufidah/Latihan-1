def make_album(artist_name, album_title, tracks=None):
    """Membangun dictionary yang mendeskripsikan sebuah album musik."""
    album_dict = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    
    # Jika jumlah lagu (tracks) diberikan, masukkan ke dalam dictionary
    if tracks:
        album_dict['tracks'] = tracks
        
    return album_dict

# Membuat tiga dictionary untuk album yang berbeda
album1 = make_album('taylor swift', 'fearless')
album2 = make_album('ed sheeran', 'divide', tracks=16)
album3 = make_album('coldplay', 'A Head Full of Dreams', tracks=11)

# Menampilkan hasil dari masing-masing album
print(album1)
print(album2)
print(album3)