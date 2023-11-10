''' Pide un numero por pantalla e indica si el numero
es un multiplo de 3 (en el sentido de que la division
de como resultado un numero entero)'''

# --- Pedir al usuario que introduzca un numero

numero = int(input("Introduce un numero: "))
# --- Comprobar si ese numero es multiplo de 3
# si es multiplo de 3, indicarlo por pantalla
if numero % 3 == 0:
    print("El numero ", numero, " es multiplo de 3")
# si no es multiplo de 3, indicarlo por pantalla
else:
    print("El numero ", numero, " no es multiplo de 3")
