import unittest
from unittest import result
import bucles

class pruebas(unittest.TestCase):
    
    def test_ejercicio_1(self): 
        objeto_1 = bucles.bucles()
        prueba1= objeto_1.Ejercicios_1("hola ")
        resultado = "hola hola hola hola hola hola hola hola hola hola "
        self.assertEqual(prueba1,resultado)
    
    def test_ejercicio_2(self): 
        objeto_2 = bucles.bucles()
        prueba2= objeto_2.Ejercicio_2(23)
        resultado = [i for i in range(1,23+1)]
        self.assertEqual(prueba2,resultado)
    
    def test_ejercicio_3(self): 
        objeto_3 = bucles.bucles()
        prueba3= objeto_3.Ejercicio_3(27)
        resultado = [i for i in range(1,27+1) if i % 2 !=0]
        self.assertEqual(prueba3,resultado)




if __name__ == '__main__':
    unittest.main()