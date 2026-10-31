prompt = "Masukkan topping pizza (ketik 'quit' untuk selesai): "

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")