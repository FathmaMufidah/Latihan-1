# Exercise 8-16: Imports

# Menggunakan cara: from module_name import function_name as fn
from printing_functions import print_models as pm, show_completed_models as scm

unprinted_designs = ['case HP', 'gantungan kunci', 'miniatur kubus']
completed_models = []

# Memanggil fungsi menggunakan nama alias yang sudah dibuat
pm(unprinted_designs, completed_models)
scm(completed_models)