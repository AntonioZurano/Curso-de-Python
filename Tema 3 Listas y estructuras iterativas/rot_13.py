'''
Desarrolla un script que recibiendo de entrada
una cadena de caracteres devuelva el texto codificado según el algoritmo ROT13.
'''

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
alfabeto_mayusculas = alfabeto.upper()
mensaje = "hola"
mensaje_comparacion = "ubyn"
mensaje_cifrado = ""


char_indice = 0
nuevo_indice = 0
# --- recorrer cada una de las letras del mensaje
for char in mensaje: 
    # compruebo si se encuentra en el alfabeto en minusuculas
    if char in alfabeto:
        # recorror el alfabeto
        for i in range(len(alfabeto)):
            # cuando ecuentre la letra guardo el indice
            if char == alfabeto[i]:
                char_indice = i

                # si la letra está en la segunda mitas del alfabeto
                if char_indice + 13 >= 26:
                    # restamos 26 para que al sumar 13 comencemos desde
                    # el comienzo del alfabeto de nuevo
                    char_indice = char_indice - 26

                # el nuevo indice cifrado será el antiguo + 13
                nuevo_indice = char_indice + 13
                # accedemos a la letra cifrada
                letra_cifrada = alfabeto[nuevo_indice]

        # añadimos la letra cifrada al mensaje cifrado
        mensaje_cifrado = mensaje_cifrado + letra_cifrada

    # compruebo si se encuentra en el alfabeto en mayúsculas
    elif char in alfabeto_mayusculas:
        # recorror el alfabeto
        for i in range(len(alfabeto_mayusculas)):
            # cuando ecuentre la letra guardo el indice
            if char == alfabeto_mayusculas[i]:
                char_indice = i

                # si la letra está en la segunda mitas del alfabeto
                if char_indice + 13 >= 26:
                    # restamos 26 para que al sumar 13 comencemos desde
                    # el comienzo del alfabeto de nuevo
                    char_indice = char_indice - 26

                # el nuevo indice cifrado será el antiguo + 13
                nuevo_indice = char_indice + 13
                # accedemos a la letra cifrada
                letra_cifrada = alfabeto_mayusculas[nuevo_indice]
        # añadimos la letra cifrada al mensaje cifrado
        mensaje_cifrado = mensaje_cifrado + letra_cifrada

    # si la letra no forma parte de las 26 letras del alfabeto latino
    # no la ciframos
    else:
        mensaje_cifrado = mensaje_cifrado + char

# Comprobamos si el mensaje cifrado y el segundo mensaje son iguales
# Si lo son:
if mensaje_cifrado == mensaje_comparacion:
    # Imprimimos que ambos mensajes son la encriptacion ROT13 el uno del otro
    print(f"Los mensajes {mensaje} y {mensaje_comparacion} son una encriptacion el uno del otro")
# Si no lo son
else:
    # Imprimimos los mensajes no son encriptacion ROT13 el uno del otro
    print(f"Los mensajes {mensaje} y {mensaje_comparacion} no son una encriptacion el uno del otro")

# --- recorrer cada una de las letras del mensaje

''' for char in mensaje:
    # --- comprobar si la letra es mayúscula o minúscula
    if char in alfabeto:
        # --- buscar la posición de la letra en el alfabeto
        posicion = alfabeto.index(char)
        # --- calcular la posición de la letra codificada
        posicion_codificada = (posicion + 13) % len(alfabeto)
        # --- añadir la letra codificada a la cadena
        cadena_codificada += alfabeto[posicion_codificada]
    elif char in alfabeto_mayuscula:
        # --- buscar la posición de la letra en el alfabeto
        posicion = alfabeto_mayuscula.index(char)
        # --- calcular la posición de la letra codificada
        posicion_codificada = (posicion + 13) % len(alfabeto_mayuscula)
        # --- añadir la letra codificada a la cadena
        cadena_codificada += alfabeto_mayuscula[posicion_codificada]
    else:
        # --- añadir la letra sin codificar a la cadena
        cadena_codificada += char

'''