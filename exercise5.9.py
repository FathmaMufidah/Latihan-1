# List username (coba kosongkan list ini nanti untuk melihat pesan 'No users')
usernames = ['admin','ari','budi','siti','joko']

# Mengecek apakah list tidak kosong
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")