


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
    
    def Ejercicio_4 (self) -> str:
        #Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
        numero = self.cadena.split("-")
        return numero[1]
    
    def Ejercicio_5(self) -> str:
        #Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
        return self.cadena[::-1]
    
    def Ejercicio_6(self,vocal:str) -> str:
        #Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
        return self.cadena.replace(vocal.lower(),vocal.upper())

    def Ejercicio_7(self) -> str:
        #Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
        
        return self.cadena[:self.cadena.find("@")] + "@ceu.es."

    def Ejercicio_8(self)->str:
        #Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
        return "son " + self.cadena[:self.cadena.find(".")] + " euros y "+ self.cadena[self.cadena.find(".")+1:] + " centavos"
        #Opcion 2
        #precio = self.cadena.split(".")
        #return f"son {precio[0]} euros y {precio[1]} centavos"

    def Ejercicio_9(self)->str:
        #Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
        return f"dia= {self.cadena[0:2]} , mes = {self.cadena[3:5]} , año = {self.cadena[6:10]}"

    def Ejercicio_10(self)->str:
        #Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
        return self.cadena.replace(",","\n")
        
    def Ejercicio_11(self,precio:float,unidades:float)->str:
        #Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
        return '{producto}:{precio:.2f} unidades={unidades:3d} , coste total = {total:.2f}'.format(producto=self.cadena,precio=precio,unidades = unidades,total = unidades*precio)











def run():
    pass

if __name__ == '__main__':
    run()