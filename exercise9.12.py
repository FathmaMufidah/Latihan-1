# Exercise 9-12: Multiple Modules

# Mengimpor class Admin dari admin_mod.py
from admin_mod import Admin

# Membuat instance dari class Admin
admin_user = Admin('rizky', 'fabian', 20, 'solo')

# Memanggil method describe_user
admin_user.describe_user()

# Memanggil method show_privileges
admin_user.privileges.show_privileges()