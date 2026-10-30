pet_1 = {'kind': 'kucing',
    'owner': 'zahrah',}

pet_2 = {'kind': 'anjing',
    'owner': 'aurel',}

pet_3 = {'kind': 'kelinci',
    'owner': 'firdan',}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Hewan ini adalah seekor {pet['kind']} dan pemiliknya adalah {pet['owner'].title()}.")