''' Crea un programa que imprima todos los numeros primos
    entre el 2 y 100. Un numero primo es un numero positivo
    y entero mayor que uno que no tiene un divisor positivo y entero 
    que no sea 1 o si mismo.
'''

# --- bucle para recorrer los numeros del 2 al 100
# --- y comprobar si son primos
for numero in range(2,101):
    # --- bucle para recorrer los numeros del 2 al numero-1
    # --- y comprobar si son divisores del numero
    primo=True
    for divisor in range(2,numero):
        if numero % divisor == 0:
            primo = False
    # --- si el contador es 0, el numero es primo
    if primo:
        print(numero, "es primo")

# --- otra forma de hacerlo
for numero in range(2,101):
    # --- bucle para recorrer los numeros del 2 al numero-1
    # --- y comprobar si son divisores del numero
    contador=0
    for divisor in range(2,numero):
        if numero % divisor == 0:
            contador += 1
            break
    # --- si el contador es 0, el numero es primo
    if contador == 0:
        print(numero, "es primo")

# --- otra forma de hacerlo
for numero in range(2,101):
    # --- bucle para recorrer los numeros del 2 al numero-1
    # --- y comprobar si son divisores del numero
    contador=0
    for divisor in range(2,numero):
        if numero % divisor == 0:
            contador += 1
            break
    # --- si el contador es 0, el numero es primo
    if contador == 0:
        print(numero, "es primo")
    else:
        print(numero, "no es primo")
