places = ["Jepang", "Swiss", "Korea Selatan", "Singapura", "Prancis"]
print("Original:", places)

print("Sorted:", sorted(places))
print("Original masih sama:", places)

places.reverse()
print("Di-reverse:", places)

places.reverse()
print("Dikembalikan ke original:", places)

places.sort()
print("Di-sort permanen (alfabet):", places)

places.sort(reverse=True)
print("Di-sort reverse permanen:", places)