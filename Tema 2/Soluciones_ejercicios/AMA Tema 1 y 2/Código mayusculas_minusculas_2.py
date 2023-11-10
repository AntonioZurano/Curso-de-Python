'''
EJERCICIOS 2B
MAYUSCULA O MINUSCULA (BONUS*):
Permite que el usuario introduzca una letra 
(del alfabeto latino) como input. Comprueba 
si esta es una mayúscula o una minúscula. 
'''

# --- Pedir al usuario una letra
letra = input("Introduce una letra: ")

# isupper()
# islower()

# --- Comprobacion del input 
if len(letra) ==1:
    # --- Condicional
    # Si es mayuscula imprimiremos que es mayuscula
    if letra.isupper():
        print("es mayuscula")
    # Si es mayuscula imprimiremos que es minuscula
    elif letra.islower():
        print("es minuscula")
    # Si es un caracter no reconocido lo indicaremos
    else: 
        print("La letra introducida no es valida")
else:
    print("Error. Debe introducir una unica letra")