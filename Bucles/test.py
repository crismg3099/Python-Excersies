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

    def test_ejercicio_4(self):
        objeto4=bucles.bucles()
        prueba4= objeto4.Ejercicio_4(18)
        resultado = "18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,"
        self.assertEqual(prueba4,resultado)
        
    def test_ejercicio_5(self):
        objeto5=bucles.bucles()
        prueba5= objeto5.Ejercicio_5(1000,10,10)
        resultado = {i:1000+(100*i) for i in range(1,10+1)}
        self.assertEqual(prueba5,resultado)
        
    def test_ejercicio_6(self):
        objeto6=bucles.bucles()
        prueba6= objeto6.Ejercicio_6(3)
        resultado = "*\n**\n***\n"
        self.assertEqual(prueba6,resultado)
        



if __name__ == '__main__':
    unittest.main()