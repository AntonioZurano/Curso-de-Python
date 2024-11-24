'''ANALISIS DE VOTACIONES:
Supongamos que tienes los resultados de una elección con los nombres
de los candidatos y la cantidad de votos obtenidos por cada uno.
Implementa un programa en Python que permita registrar los votos,
mostrar la lista completa de candidatos y sus votos, encontrar al
candidato ganador (con más votos) y calcular el porcentaje de votos que
obtuvo cada candidato.'''
#diccionario de votos vacio
votos = {}
continuar = True

while continuar:
    print("Seleccione una opción:")
    print("1. Registrar un voto")
    print("2. Mostrar la lista completa de candidatos y sus votos")
    print("3. Encontrar al candidato ganador")
    print("4. Calcular el porcentaje de votos que obtuvo cada candidato")
    print("5. Salir")
    opcion = input("Ingrese el número de la opción que desea realizar: ")

    #registrar un voto
    if opcion == "1":
        candidato = input("Ingrese el nombre del candidato: ")
        votos_obtenidos = int(input("Ingrese la cantidad de votos obtenidos por el candidato: "))
        votos[candidato] = votos_obtenidos
        print(f"Voto registrado con éxito.")
        print(votos)

    #mostrar la lista completa de candidatos y sus votos
    elif opcion == "2":
        print("Lista completa de candidatos y sus votos:")
        for candidato, votos_obtenidos in votos.items():
            print(f"Candidato: {candidato}, Votos obtenidos: {votos_obtenidos}")

    #encontrar al candidato ganador
    elif opcion == "3":
        candidato_ganador = max(votos, key=votos.get)
        votos_ganador = votos[candidato_ganador]
        print("Candidato ganador:")
        print(f"Candidato: {candidato_ganador}, Votos obtenidos: {votos_ganador}")

    #calcular el porcentaje de votos que obtuvo cada candidato
    elif opcion == "4":
        total_votos = sum(votos.values())
        print("Porcentaje de votos que obtuvo cada candidato:")
        for candidato, votos_obtenidos in votos.items():
            porcentaje_votos = (votos_obtenidos / total_votos) * 100
            print(f"Candidato: {candidato}, Porcentaje de votos: {porcentaje_votos:.2f}%")

    #salir
    elif opcion == "5":
        continuar = False
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        print("")
