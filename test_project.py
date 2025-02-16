import pytest
from project import get_data  
from project import format_price
from project import is_valid_currency_code

def test_format_price():
    assert format_price("1,234.56") == 1234.56
    assert format_price("100") == 100.0
    assert format_price("0.99") == 0.99
    assert format_price("10,000.00") == 10000.00

def test_get_data():
    result = get_data("EUR", "USD")

    assert isinstance(result, dict)
    assert "price" in result
    assert "title" in result
    assert "Convert Euros to US Dollars" in result["title"]

def test_is_valid_currency_code():
    valid_codes = ["USD", "EUR", "GBP", "JPY", "CAD"]

    assert is_valid_currency_code("USD", valid_codes) == True
    assert is_valid_currency_code("EUR", valid_codes) == True
    assert is_valid_currency_code("XYZ", valid_codes) == False
    assert is_valid_currency_code("", valid_codes) == False
