'''
Implementa un programa en Python que permita registrar y mantener un 
seguimiento de los puntajes de un juego. El programa debe permitir a los 
jugadores ingresar sus nombres y puntajes, almacenarlos en un 
diccionario y proporcionar funcionalidades para mostrar el puntaje más 
alto, el promedio de puntajes y la cantidad total de jugadores.
'''

#diccionario de puntajes vacio
registros ={}
continuar = True


#seguimiento de los puntajes --> actualizados
while continuar:
    # Pedir al usuario su nombre
    nombre = input("Ingrese el nombre del jugador: (o introduca 'salir' para terminar): ")
    if nombre.lower() == "salir":
        continuar = False
    else:
        puntaje = int(input("Ingrese el puntaje del jugador: "))
        registros[nombre] = puntaje
    
   # print(registros)
    jugador_mas_alto = max(registros, key=registros.get)
    puntaje_mas_alto = registros[jugador_mas_alto]
    print("Puntaje más alto:")
    print(f"Jugador: {jugador_mas_alto}")

    # Obtener el promedio de puntajes
    total_puntajes = sum(registros.values()) #sumamos los valores de los puntajes
    cantidad_jugadores = len(registros) #contamos la cantidad de jugadores
    promedio = total_puntajes / cantidad_jugadores #calculamos el promedio
    print("Promedio de puntajes:") #imprimimos el promedio
    print(promedio) #imprimimos el promedio

    # Mostrar la cantidad total de jugadores
    print("Cantidad total de jugadores:")
    print(cantidad_jugadores)
    print("")


