my_foods = ['pizza', 'bakso', 'ice cream']
friend_foods = my_foods[:]

my_foods.append('es teh')
friend_foods.append('ayam geprek')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite food are:")
for food in friend_foods:
    print(food)
