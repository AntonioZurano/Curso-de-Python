'''
EJERCICIOS 2B
MAYUSCULA O MINUSCULA (BONUS*):
Permite que el usuario introduzca una letra
(del alfabeto latino) como input. Comprueba si esta 
es una mayúscula o una minúscula. 
'''

# Pedimos al usuario que introduzca una letra
letra = input("Introduce una letra: ")

# isupper() nos devuelve True si la letra es mayuscula
# islower() nos devuelve True si la letra es minuscula

# --- Comprobacion del input
if len(letra) == 1:
    # --- Condicional
    # Si es mayuscula imprimiremos que es mayuscula
    if letra.isupper():
        print("Es mayuscula")
    # Si es minuscula imprimiremos que es minuscula
    elif letra.islower():
        print("Es minuscula")   
    # Si no es ninguna de las dos imprimiremos que no es una letra
    else:
        print("La letra introducida no es válida")
else:
    print("Introduce solo una letra")
    exit()