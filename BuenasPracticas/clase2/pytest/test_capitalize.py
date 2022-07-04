import pytest
# def capital_case(x):
#     return x.capitalize()

def capital_case(x):
    if not isinstance(x,str):
        raise TypeError("el tipo de dato no es correcto")
    return x.capitalize()


def test_capital_case():
    assert capital_case('desarrollo')=='Desarrollo' #-- sale . esta bien en el de abajo F esta mal
    assert capital_case('desarrollo')=='desarrollo' # F esta mal
    # assert capital_case(9)=='desarrollo'    -- TypeError

def test_control_non_string():
    with pytest.raises(TypeError):
        capital_case(9)
