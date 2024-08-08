'''Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con 
los números primos de la lista original. Además, el script debe devolver el número total de 
números primos encontrados y la suma de los números primos encontrados '''

# --- lista de numeros enteros
numeros_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

# --- lista vacia de numeros primos
numeros_primos = []
# + numero total de numeros primos (contador)
total_primos = 0
# + suma de los numeros primos (contador)
suma_primos = 0
# --- bucle para recorrer la lista de numeros enteros
for numero in numeros_enteros:
    # + inicializar la variable primo a True
    primo = True
    #--- comprobar si cada numero es primo
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    if primo == True:
        # si es primo lo añadimos a la lista de numeros primos
        numeros_primos.append(numero)
        # + incrementar el contador de numeros primos
        total_primos += 1
        # + incrementar la suma de numeros primos
        suma_primos += numero

# --- mostrar el resultado
print("Lista de numeros enteros:", numeros_enteros)
print("Lista de numeros primos:", numeros_primos)
print("Numero total de numeros primos:", total_primos)
print("Numero total de numeros primos:", len(numeros_primos))
print("Suma de numeros primos:", suma_primos)
print("Suma de numeros primos:", sum(numeros_primos))


