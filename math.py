import math
SEPARADOR = ("*" * 20) + "\n"
'''
Ejemplo para ilustrar la importancia de la libreria math en Python 3 
Demuestra el uso de: floor(x),trunc(x),ceil(x),round(x),factorial(x),pow(x,y),sqrt(x) y pi
'''

valorFlotante = float(input("Introduce un valor con fraccion decimal:\n"))
print(f"El siguiente entero hacia arriba de {valorFlotante} es {math.ceil(valorFlotante)}")
print(SEPARADOR)
print(f"El siguiente entero hacia abajo de {valorFlotante} es {math.floor(valorFlotante)}")
print(SEPARADOR)
print(f"La parte entera truncada de {valorFlotante} es {math.trunc(valorFlotante)}") #Equivalente a floor() para positvos, y ceil() para negativos por que se mueve hacia el 0
print(SEPARADOR * 2)
pass
valorNumerico = int(input("Dame un valor entero:\n"))
print(f"La raiz cuadrada de {valorNumerico} es igual a {math.sqrt(valorNumerico)}")
print(SEPARADOR)
print(f"El factorial de {valorNumerico} es igual a {math.factorial(valorNumerico)}")
potencia = int(input("Dame un valor entero:\n"))
print(f"El resultado de elevar {valorNumerico} a la {potencia} potencia es igual a {math.pow(valorNumerico,potencia)}")
print(SEPARADOR * 2)
pass


print(f"El valor de Pi es {math.pi}")