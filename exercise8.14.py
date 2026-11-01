def make_car(manufacturer, model, **car_info):
    """Membangun dictionary yang menyimpan informasi tentang sebuah mobil."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# Memanggil fungsi dengan informasi wajib dan tambahan keyword arguments
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)