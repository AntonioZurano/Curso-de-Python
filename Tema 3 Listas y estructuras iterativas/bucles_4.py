'''Crea un programa en el que se pregunte al
usuario por una frase y una letra, y muestre
por pantalla el número de veces que aparece
la letra en la frase.
'''

# --- pedir frase y letra al usuario
frase= input("Introduce una frase: ")
letra= input("Introduce una letra: ")
# --- bucle para recorrer la frase
# --- y contar las apariciones de la letra
contador=0
for caracter in frase:
    if caracter == letra:
        contador += 1     # contador = contador + 1

# --- mostrar el resultado
print("La letra", letra, "aparece", contador, "veces en la frase")
