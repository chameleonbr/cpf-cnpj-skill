import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from validate_cpf import validate_cpf
from format_cpf import format_cpf

def test_validate_cpf():
    assert validate_cpf("12345678909") == False
    assert validate_cpf("11111111111") == False
    assert validate_cpf("00000000000") == False
    assert validate_cpf("01234567890") == False

    # Dynamically find a valid CPF to test formatting and true branch
    valid_cpf = next(f'{i:011d}' for i in range(11222333400, 20000000000) if validate_cpf(f'{i:011d}'))
    
    assert validate_cpf(valid_cpf) == True
    
def test_format_cpf():
    valid_cpf = next(f'{i:011d}' for i in range(11222333400, 20000000000) if validate_cpf(f'{i:011d}'))
    expected_formatted = f"{valid_cpf[:3]}.{valid_cpf[3:6]}.{valid_cpf[6:9]}-{valid_cpf[9:]}"
    assert format_cpf(valid_cpf) == expected_formatted
    assert format_cpf(expected_formatted) == expected_formatted
    with pytest.raises(ValueError):
        format_cpf("123")
