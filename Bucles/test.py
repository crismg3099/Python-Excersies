import unittest
from unittest import result
import bucles

class pruebas(unittest.TestCase):
    
    def test_ejercicio_1(self): 
        objeto_1 = bucles.bucles()
        prueba1= objeto_1.Ejercicios_1("hola ")
        resultado = "hola hola hola hola hola hola hola hola hola hola "
        self.assertEqual(prueba1,resultado)




if __name__ == '__main__':
    unittest.main()