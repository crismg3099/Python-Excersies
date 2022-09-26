
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
    
    def Ejercicio_2(self,edad:int) -> list:
        #Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
            tiempo = []
            for i in range(1,edad+1):
                tiempo.append(i)
            return tiempo
    
    def Ejercicio_3(self,numero:int) -> list:
        #Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
        numeros = []
        for i in range (1,numero+1):
            if i % 2 != 0:
                numeros.append(i)
        return numeros





