from exercise11_1_city_functions import city_country


def test_city_country():
    """Apakah lokasi seperti 'santiago' dan 'chile' terformat dengan benar?"""
    formatted_location = city_country('santiago', 'chile')
    assert formatted_location == 'Santiago, Chile'


def test_city_country_population():
    """Apakah lokasi dengan populasi terformat dengan benar?"""
    formatted_location = city_country('santiago', 'chile', population='5000000')
    assert formatted_location == 'Santiago, Chile – population 5000000'