

'''
    pip install pytest
    import pytest
    ejecutar---- pytest test_methods.py
    se ejecutan los metodos:
        def test_addName():
        def test_addNameNumber():
        def test_addNameInvalid():
        def test_addNumber():
        def test_checkMoney():
    
'''

import pytest

class InvalidName(Exception):
    pass
class InvalidQuery(Exception):
    pass

def addName(name:str):
    """ AÑADIR NOMBRE, PASAR POR PARAMETRO UN NOMBRE Y SI NO EXISTE SE LE AÑADE

    Args:
        name (str): Nombre que queremos insertar

    Raises:
        TypeError: No has insertado un valor de tipo str
        InvalidName: Nombre ya existe

    Returns:
        _type_: Lista con nuevo nombre
    """
    names=['Juan','Pepe','Lucia']
    if isinstance(name,str) & (name not in names):
        names.append(name)
        return names
    elif not isinstance(name,str):
        raise TypeError("Incorrect type data")
    elif name in names:
        raise InvalidName("The name exists")


def addNumber(number:int):
    """ AÑADIR TELEFONO

    Args:
        number (int): NUMERO DE TELEONO QUE QUIERES INSERTAR

    Returns:
        _type_: TRUE O FALSE
    """
    phone=str(number)
    if len(phone)==9:
        return True


def checkMoney(name:str):
    """ COMPROBAR DINERO, SI EL NOMBRE EXISTE TE MUESTRA EL DINERO

    Args:
        name (str): NOMBRE DEL CLIENTE

    Raises:
        InvalidQuery: NO EXISTE EL NOMBRE DEL CLIENTE

    Returns:
        _type_: int -- dinero
    """
    bill={'Ruben':100,'Jonathan':150}
    for c,v in bill.items():
        if c==(name):
            return v 
        else:
            raise InvalidQuery("Error, the query could not be done")


def test_addName():
    assert addName('Jonathan')==['Juan','Pepe','Lucia','Jonathan']

def test_addNameNumber():
    with pytest.raises(TypeError):
        addName(4)

def test_addNameInvalid():
    with pytest.raises(InvalidName):
        addName('Pepe')

def test_addNumber():
    assert addNumber(123456789)
    # assert addNumber(123)

def test_checkMoney():
    assert checkMoney("Ruben")==100
    # assert checkMoney("Ruben")==111
    # assert checkMoney("Joa")==111


'''
    import unittest
    ejecutar---- python test_methods.py
    Tiene que tener:
     la clase (unittest.TestCase)
     if __name__ == '__main__':
        unittest.main()
    se ejecutan los metodos:
        def test_checkName(self):
        def test_checkNumber(self):
        def test_addNames(self):  
        def test_checkmoney(self):   
        def test_checkType(self):   
'''
import unittest

class TestUnittestPractica(unittest.TestCase):

    def test_checkName(self):
        self.assertIn("Juan",['Juan','Pepe','Lucia'])
        # self.assertIn("Jonathan",['Juan','Pepe','Lucia'])
     
    def test_checkNumber(self):
        number=str(123456789)
        self.assertTrue(len(number)==9)

    def test_addNames(self):
        childrens= ['Bea','Pepe','Lucia']
        children='David'
        if children is None:
            self.assertIsNone(children,"error")
        else:
            childrens.append(children)
    def test_checkmoney(self):
        bill={'Ruben':100,'Jonathan':150}
        name='Jonathan'
        if self.assertEqual(name,'Jonathan'):
            print(150)
    
    def test_checkType(self):
        x=3
        y='na'
        with self.assertRaises(TypeError):
            resultado=x + y
    
    
if __name__ == '__main__':
    unittest.main()

