def make_sandwich(*items):
    """Meringkas item/topping sandwich yang diinginkan pelanggan."""
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in items:
        print(f"- {item}")

# Memanggil fungsi tiga kali dengan jumlah argumen yang berbeda-beda
make_sandwich('keju', 'tomat', 'selada')
make_sandwich('daging sapi', 'keju ekstra')
make_sandwich('ayam', 'mayo', 'timun', 'bawang bombay')