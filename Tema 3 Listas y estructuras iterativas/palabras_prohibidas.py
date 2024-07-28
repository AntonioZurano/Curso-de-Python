'''Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras. 
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga 
aquellas palabras que no tienen ninguna letra prohibida. '''

# --- Crear lista de palabras aleatorias y lista de letras prohibidas
# --- + lista de palabras filtradas

palabras_aleatorias = ["casa", "perro", "gato", "libro", "ratón"]
letras_prohibidas = ["a",  "u"]
palabras_filtradas = []

# --- Bucle para recorre la lista de palabras
for palabra in palabras_aleatorias:
    incluir= True
    # --- Bucle para recorrer cada palabra
    for letra in palabra:
        # Bucle para comprobar si cada objeto tiene alguna letra prohibida.
        for letra_prohibida in letras_prohibidas:
        ## si no tiene letra prohibida lo incluimos en la lista filtrada
            if letra == letra_prohibida:
                incluir = False
    if incluir == True:
        palabras_filtradas.append(palabra)


# --- Imprimimos por pantalla las tres listas
print("Lista de palabras aleatorias:", palabras_aleatorias)
print("Lista de letras prohibidas:", letras_prohibidas)
print("Lista de palabras filtradas:", palabras_filtradas)
