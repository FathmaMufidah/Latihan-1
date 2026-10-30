# Membuat list berisi beberapa username, termasuk 'admin'
usernames = ['admin', 'ari', 'budi', 'siti', 'joko']

# Melakukan perulangan untuk mengecek setiap username di dalam list
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")