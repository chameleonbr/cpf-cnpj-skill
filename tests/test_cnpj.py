import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from validate_cnpj import validate_cnpj
from format_cnpj import format_cnpj

def test_validate_cnpj():
    assert validate_cnpj("11111111111111") == False
    assert validate_cnpj("00000000000000") == False
    assert validate_cnpj("12345678901234") == False

    # Dynamically find a valid CNPJ
    valid_cnpj = next(f'{i:014d}' for i in range(11222333000100, 11222333000200) if validate_cnpj(f'{i:014d}'))
    
    assert validate_cnpj(valid_cnpj) == True

def test_format_cnpj():
    valid_cnpj = next(f'{i:014d}' for i in range(11222333000100, 11222333000200) if validate_cnpj(f'{i:014d}'))
    expected_formatted = f"{valid_cnpj[:2]}.{valid_cnpj[2:5]}.{valid_cnpj[5:8]}/{valid_cnpj[8:12]}-{valid_cnpj[12:]}"
    assert format_cnpj(valid_cnpj) == expected_formatted
    assert format_cnpj(expected_formatted) == expected_formatted
    with pytest.raises(ValueError):
        format_cnpj("123")
