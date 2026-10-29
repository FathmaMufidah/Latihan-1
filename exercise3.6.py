guest_list = ["B.J.Habibie", "Albert Einstain", "Nikola Tesla"]
print("Good newas, we got a bigger table!")

# Menambah tamu di awal, tengah, dan akhir
guest_list.insert(0, "Isaac Newton")
guest_list.insert(2, "Syahrini")
guest_list.append("Ayu Ting-Ting")

# Cetak ulang undangan
for tamu in guest_list:
    print(f"For {tamu}, come join us for dinner.")
