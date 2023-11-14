'''
EJERCICIOS 2B
MAYUSCULA O MINUSCULA (BONUS*):
Permite que el usuario introduzca una letra
(del alfabeto latino) como input. Comprueba si esta 
es una mayúscula o una minúscula. 
'''

# Pedimos al usuario que introduzca una letra
letra = input("Introduce una letra: ")


#ord() nos devuelve el valor ascii de un caracter


#mayuscula 65 -- 90
#minuscula 97 -- 122

if 65 <= ord(letra) <= 90:
    print("Es mayuscula")
elif 97 <= ord(letra) <= 122:
    print("Es minuscula")
else:
    print("La letra introducida no es válida") 