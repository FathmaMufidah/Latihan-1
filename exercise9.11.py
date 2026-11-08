# Mengimpor class Admin dari modul user.py
from user import Admin

# Membuat instance dari class Admin
admin_user = Admin('zahrah', 'cintani', 18, 'solo')

# Memanggil method describe_user untuk membuktikan akses parent class
admin_user.describe_user()

# Memanggil method show_privileges melalui instance privileges
admin_user.privileges.show_privileges()