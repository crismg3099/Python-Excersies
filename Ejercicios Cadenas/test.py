
import unittest
from unittest import result
import Ejercicio_candenas

class pruebas_unitarias(unittest.TestCase):
    
    def test_ejercicio1(self):
        Nombre = Ejercicio_candenas.Cadenas("Christian")
        resultado =Nombre.Ejercicio_1(3)
        self.assertEqual(resultado,"ChristianChristianChristian")

    def test_ejercicio2(self):
        nombre = Ejercicio_candenas.Cadenas("cHristian Macosay")
        resultado = nombre.Ejercicio_2()
        self.assertEqual(resultado,"christian macosay-CHRISTIAN MACOSAY-Christian Macosay")



if __name__ == '__main__':
    unittest.main()