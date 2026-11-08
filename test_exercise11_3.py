# test_exercise11_3.py

import pytest
from exercise11_3_employee import Employee


@pytest.fixture
def employee_single():
    """Fixture untuk menyediakan instance Employee yang akan digunakan di setiap tes."""
    return Employee('Fathma', 'Mufidah', 60000)


def test_give_default_raise(employee_single):
    """Menguji apakah kenaikan gaji default ($5,000) bekerja dengan benar."""
    employee_single.give_raise()
    assert employee_single.annual_salary == 65000


def test_give_custom_raise(employee_single):
    """Menguji apakah kenaikan gaji kustom bekerja dengan benar."""
    employee_single.give_raise(10000)
    assert employee_single.annual_salary == 70000