'''
    Este scripts sirve para comprobar los metodos

    Tienes que tener instalado y luego importar en el scripts:
        ``pip install pytest``

        ``import pytest``
    
    Las funciones tienen que llevar : 
        test_nombreFuncion()
    
    Para ejecutar::
        ``pytest test_methods.py``
    
    Se ejecutan los metodos:
        * def test_addName():
        
        * def test_addNameNumber():

        * def test_addNameInvalid():

        * def test_addNumber():
            
        * def test_checkMoney():

'''
import pytest
from methods import *


def test_addName():
    """Metodo para comprobar el metodo addName de methods,py
    """
    assert addName('Jonathan')==['Juan','Pepe','Lucia','Jonathan']

def test_addNameNumber():
    """Metodo para comprobar el metodo addName de methods,py si añades un numero
    """
    with pytest.raises(TypeError):
        addName(4)

def test_addNameInvalid():
    """Metodo para comprobar el metodo addName de methods,py si añades un nombre no valido
    """
    with pytest.raises(InvalidName):
        addName('Pepe')

def test_addNumber():
    """Metodo para comprobar el metodo addNumber de methods,py
    """
    assert addNumber(123456789)
    # assert addNumber(123)

def test_checkMoney():
    """Metodo para comprobar el metodo checkMoney de methods,py
    """
    assert checkMoney("Ruben")==100
    # assert checkMoney("Ruben")==111
    # assert checkMoney("Joa")==111
