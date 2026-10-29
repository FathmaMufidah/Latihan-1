guest_list = ["B.J.Habibie", "Albert Einstein", "Rafi Ahmad"]

# Tamu yang tidak bisa hadir
tidak_hadir = guest_list[2]
print(f"Sorry, {tidak_hadir} I cannot attend.")

# Mengganti tamu yang tidak hadir dengan tamu baru
guest_list[2] = "Nikola Tesla"

# Mengirim undangan baru
print(f"For {guest_list[0]}, You are invinted to dinner with me.")
print(f"For {guest_list[1]}, You are invinted to dinner with me")
print(f"For {guest_list[2]}, You are invinted to dinner with me.")