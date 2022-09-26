
from ast import Pass
import re


class bucles():
    def __init__(self):
        pass

    def Ejercicios_1(self,palabra) -> str:
        #Ejercicio 1 Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
        resultado:str =""
        for i in range(0,10):
            resultado= resultado + palabra
        
        return  resultado
            

