
import unittest
from unittest import result
import Ejercicio_candenas

class pruebas_unitarias(unittest.TestCase):
    
    def test_ejercicio1(self):
        Nombre = Ejercicio_candenas.Cadenas("Christian")
        resultado =Nombre.Ejercicio_1(3)
        self.assertEqual(resultado,"ChristianChristianChristian")



if __name__ == '__main__':
    unittest.main()