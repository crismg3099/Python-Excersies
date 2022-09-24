


class Cadenas:

    def __init__(self,cadena:str) :
        self.cadena = cadena
        
        

    def Ejercicio_1(self,n:int) -> str:
        #Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
        return self.cadena * n
    
    def Ejercicio_2 (self) -> str :
        #Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
        return self.cadena.lower() +"-"+self.cadena.upper()+"-"+self.cadena.title()

    def Ejercicio_3(self) -> str :
        #Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
        return f"{self.cadena.upper()} tiene {len(self.cadena)} letras " 





def run():
    pass

if __name__ == '__main__':
    run()