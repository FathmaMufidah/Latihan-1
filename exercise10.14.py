# Exercise 10-14: Verify User

import json
from pathlib import Path


def get_stored_username(path):
    """Mendapatkan username yang tersimpan jika ada."""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        username = json.loads(contents)
        return username
    return None


def get_new_username(path):
    """Meminta username baru dan menyimpannya ke file."""
    username = input("Masukkan nama Anda: ")
    contents = json.dumps(username)
    path.write_text(contents, encoding='utf-8')
    return username


def greet_user():
    """Menyapa pengguna dan memverifikasi identitasnya."""
    path = Path('TUGAS/username.json')
    username = get_stored_username(path)

    if username:
        correct = input(f"Apakah Anda adalah {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingat Anda saat kembali nanti, {username}!")
    else:
        username = get_new_username(path)
        print(f"Kami akan mengingat Anda saat kembali nanti, {username}!")


# Menjalankan fungsi utama
greet_user()