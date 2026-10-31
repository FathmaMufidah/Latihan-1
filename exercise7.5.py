prompt = "Berapa usia Anda?"
prompt += "\n(Ketik 'quit' jika sudah selesai) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    
    age = int(age)
    
    if age < 3:
        print("Tiket Anda gratis!\n")
    elif age <= 12:
        print("Harga tiket Anda adalah $10.\n")
    else:
        print("Harga tiket Anda adalah $15.\n")