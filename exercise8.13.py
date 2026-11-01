def build_profile(first, last, **user_info):
    """Membangun dictionary yang berisi segala hal tentang diri kita."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Membuat profil diri sendiri menggunakan nama dan 3 informasi tambahan
my_profile = build_profile(
    'fathma', 
    'mufidah', 
    university='universitas sebelas maret', 
    major='teknik industri', 
    hobby='merajut'
)

print(my_profile)