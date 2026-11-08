def city_country(city, country, population=''):
    """Mengembalikan string berformat 'City, Country - population xxx'."""
    if population:
        formatted_location = f"{city.title()}, {country.title()} – population {population}"
    else:
        formatted_location = f"{city.title()}, {country.title()}"
    return formatted_location