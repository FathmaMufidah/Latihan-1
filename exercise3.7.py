guest_list = ["Isaac Newton", "B.J.Habibie", "Syahrini", "ALbert Einstain", "Nikola Tesla", "Ayu Ting-Ting"]
print("Sorry, the new table didn't arrive, so only 2 people can be invinted.")

while len(guest_list) > 2:
    dihapus = guest_list.pop()
    print(f"Sorry {dihapus}, I cannot invite you.")

print(f"{guest_list[0]}, You are still invited.")
print(f"{guest_list[1]}, You are still invited.")

del guest_list[0]
del guest_list[0]
print(guest_list) # Hasilnya list kosong[]