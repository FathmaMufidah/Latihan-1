person_1 = {'first_name': 'zahrah', 
    'last_name': 'cintani', 
    'age': 18, 
    'city': 'tangerang',}

person_2 = {'first_name': 'ratna', 
    'last_name': 'dewi', 
    'age': 50, 
    'city': 'yogyakarta',}

person_3 = {'first_name': 'ari', 
    'last_name': 'wibowo', 
    'age': 30, 
    'city': 'bandung',}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Nama: {full_name.title()}")
    print(f"Usia: {person['age']}")
    print(f"Kota: {person['city'].title()}\n")