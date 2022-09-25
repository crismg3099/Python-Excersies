
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
    
    def test_ejercicio3(self):
        nombre = Ejercicio_candenas.Cadenas("Christian")
        resultado = nombre.Ejercicio_3()
        self.assertEqual(resultado,"CHRISTIAN tiene 9 letras ")

    def test_Ejercicio4(self):
        n = Ejercicio_candenas.Cadenas("+34-913724710-56")
        numero = n.Ejercicio_4()
        self.assertEqual(numero,"913724710")

    def test_Ejercicio5(self):
        objeto5= Ejercicio_candenas.Cadenas("Hola")
        palabra1= objeto5.Ejercicio_5()
        palabra2 = "aloH"
        self.assertEqual(palabra1,palabra2) 

    def test_Ejercicio6(self):
        objeto6= Ejercicio_candenas.Cadenas("Hola")
        palabra1= objeto6.Ejercicio_6("a")
        palabra2 = "HolA"
        self.assertEqual(palabra1,palabra2) 

    def test_Ejercicio7(self):
        objeto7= Ejercicio_candenas.Cadenas("christian@gmail.com")
        palabra1= objeto7.Ejercicio_7()
        palabra2 = "christian@ceu.es."
        self.assertEqual(palabra1,palabra2) 

    def test_Ejercicio8(self):
        objeto8= Ejercicio_candenas.Cadenas("452.65")
        palabra1= objeto8.Ejercicio_8()
        palabra2 = "son 452 euros y 65 centavos"
        self.assertEqual(palabra1,palabra2) 

    def test_Ejercicio9(self):
        objeto9= Ejercicio_candenas.Cadenas("30/03/1999")
        palabra1= objeto9.Ejercicio_9()
        palabra2 = "dia= 30 , mes = 03 , año = 1999"
        self.assertEqual(palabra1,palabra2) 

    def test_Ejercicio10(self):
        objeto10= Ejercicio_candenas.Cadenas("manzanas,peras,platanos")
        palabra1= objeto10.Ejercicio_10()
        palabra2 = "manzanas\nperas\nplatanos"
        self.assertEqual(palabra1,palabra2) 

    def test_Ejercicio11(self):
        objeto11= Ejercicio_candenas.Cadenas("Juguete")
        palabra1= objeto11.Ejercicio_11(25,5)
        palabra2 = "Juguete:25.00 unidades=  5 , coste total = 125.00"
        self.assertEqual(palabra1,palabra2) 



if __name__ == '__main__':
    unittest.main()