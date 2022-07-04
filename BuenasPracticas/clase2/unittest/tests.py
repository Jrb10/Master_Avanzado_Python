from re import A
from funciones import calcula_media

import unittest

# python-m unittest tests
# python-m unittest -v tests

# class TestCalcularMedia(unittest.TestCase):
#     def test_1(self):
#         resultado=calcula_media([5,5,5])
#         self.assertEqual(resultado,5)
    
#     def test_2(self):
#         resultado=calcula_media([5,5,5])
#         self.assertEqual(resultado,10)

class TestEjemplos(unittest.TestCase):
    def setUp(self):
        print("entra en el setup")

    def tearDown(self) -> None:
        print("entra en el down")

    def test_in(self):
        self.assertIn(4, [1,2,3])

    def test_is(self):
        a=3
        b=a 
        self.assertIs(a,b)

    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            x=0/0

if __name__=='__main__':
    unittest.main()

# .assertEqual(a, b): Verifica la igualdad de ambos valores.
# .assertTrue(x): Verifica que el valor es True.
# .assertFalse(x): Verifica que el valor es False.
# .assertIs(a, b): Verifica que ambas variables son la misma (ver operador is).
# .assertIsNone(x): Verifica que el valor es None.
# .assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in).
# .assertIsInstance(a, b): Verifica que a es una instancia de b
# .assertRaises(x): Verifica que se lanza una excepción.