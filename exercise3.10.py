gunung = ["Merapi", "Semeru", "Rinjani", "Kerinci"]
gunung.append("Bromo")
gunung.insert(1, "Lawu")
del gunung [0]
terakhir = gunung.pop()
print("Sisa gunung:", gunung)
print("Jumlah gunung:", len(gunung))
print("Urutan alfabet:", sorted(gunung))