my_pizzas = ["pepperoni", "meatlovers", "cheese"]
friend_pizzas = my_pizzas[:]
# Menyalin list menggunakan slice

# Menambahkan pizza baru ke masing-masing list
my_pizzas.append("hawaiian")
friend_pizzas.append("supreme")

# Mencetak pizza saya
print("Pizza favorit saya adalah:")
for pizza in my_pizzas:
    print(pizza)

# Mencetak pizza temen saya
print("\nPizza favorit teman saya adalah:")
for pizza in friend_pizzas:
    print(pizza)
    