
from ast import Pass
import re
from unittest import result


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
    def Ejercicio_4(self,numero:int) -> str:
        #Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
        resultado=""
        for i in range(numero,0,-1):
            resultado = resultado + str(i) +","
        return resultado
    def Ejercicio_5(self,cantidad,interes,años) -> dict:
        #Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
        inversiones = {}
        acumulado = 0
        for i in range(1,años+1):
            acumulado =acumulado + (cantidad * (interes/100))
            inversiones[i]= cantidad + acumulado
        return inversiones        

    def Ejercicio_6(self,numero:int) -> str:
        #Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
        resultado = ""
        for i in range (1,numero+1):
            resultado =resultado + ("*" * i) + "\n" 
        return resultado
    
    def Ejercicio_7(self,tabla:int):
        #Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
        pass




