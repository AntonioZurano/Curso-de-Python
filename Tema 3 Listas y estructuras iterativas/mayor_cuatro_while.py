'''
Pide a usuario 4 números y devuelve 
los números introducidos en orden 
descendente. Para ello puedes usar listas y bucles while.'''


# --- inicializar una lista de numeros
lista_numeros = []
terminado=False
# --- Crear un bucle para ir pidiendo los números
# --- y añadiendolos a la lista
while terminado == False:
    # pido el numero
    numero = input("Dime un numero: ")
    # compruebo que sea un numero
    if numero.isnumeric() == False:
        print("Eso no es un numero")
        continue
    # lo convierto a entero
    numero = int(numero)

    # lo añado a la lista de numeros
    lista_numeros.append(numero)

    if len(lista_numeros) == 4:
        terminado = True

# output: la lista con los cuatro numeros
#print(lista_numeros)
# --- imprimo el mayor numero de la lista por pantalla
#print("El número mas alto es",max(lista_numeros))
# --- imprimir la lista ordenada ascendentemente
#print("La lista ordenada es",sorted(lista_numeros))

# --- otra forma de ordenar la lista e imprimir el mayor
lista_numeros.sort()
print("El numero mas alto es",lista_numeros[-1],"y la lista ordenada es", lista_numeros)