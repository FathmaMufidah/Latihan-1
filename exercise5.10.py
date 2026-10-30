current_users = ['admin', 'ari', 'budi', 'siti', 'joko']
new_users = ['arif', 'rudi', 'dewi', 'dodi', 'budi']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah digunakan. Silakan masukkan username lain!")
    else:
        print(f"Username '{new_user}' tersedia dan bisa digunakan.")