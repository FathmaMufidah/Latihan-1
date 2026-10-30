rivers = {'bengawan solo': 'indonesia',
    'mahakam': 'indonesia',
    'mississippi': 'amerika serikat',}

for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melewati negara {country.title()}.")

print("\nDaftar Sungai:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nDaftar Negara:")
for country in rivers.values():
    print(f"- {country.title()}")