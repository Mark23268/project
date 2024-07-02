import pytest
from project import calculate_fuel_cost, convert_to_float, is_valid_input

def test_calculate_fuel_cost():
    assert calculate_fuel_cost(10, 100, 3) == 30
    assert calculate_fuel_cost(25, 250, 4) == 40
    assert calculate_fuel_cost(0, 100, 3) is None
    assert calculate_fuel_cost(10, 100, 'a') is None

def test_convert_to_float():
    assert convert_to_float("10.5") == 10.5
    assert convert_to_float("abc") is None
    assert convert_to_float("") is None

def test_is_valid_input():
    assert is_valid_input(10.5, 100, 3) == True
    assert is_valid_input(None, 100, 3) == False
    assert is_valid_input(10.5, None, 3) == False
    assert is_valid_input(10.5, 100, None) == False

if __name__ == "__main__":
    pytest.main()
