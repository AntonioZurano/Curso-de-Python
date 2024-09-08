'''
Pide a usuario 4 números y devuelve 
los números introducidos en orden 
descendente. Para ello puedes usar listas y bucles for.'''

# --- inicializar una lista de numeros
lista_numeros = []

# --- Crear un bucle para ir pidiendo los números
# --- y añadiendolos a la lista

for i in range(0,4):
    # pido el numero
    numero = input("Dime un numero: ")
    # lo convierto a entero
    numero = int(numero)
    # lo añado a la lista de numeros
    lista_numeros.append(numero)
# output: lista con cuatro numeros
print(lista_numeros)
# --- imprimo el mayor numero de la lista por pantalla
print("El número mas alto es",max(lista_numeros))
# --- imprimir la lista ordenada 
print("La lista ordenada en orden ascendente son",sorted(lista_numeros))
