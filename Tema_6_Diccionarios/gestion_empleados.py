'''GESTION DE EMPLEADOS 
Imagina que eres el gerente de recursos humanos de una empresa y 
necesitas gestionar la información de los empleados. Cada empleado 
tiene un nombre, salario y departamento al que pertenece. Implementa 
un programa en Python que permita agregar nuevos empleados, 
actualizar el salario de un empleado existente, mostrar la lista completa 
de empleados y calcular el promedio salarial por departamento. 
ANÁLISIS DE VOTACIONES: 
Supongamos que tienes los resultados de una elección con los nombres 
de los candidatos y la cantidad de votos obtenidos por cada uno. 
Implementa un programa en Python que permita registrar los votos, 
mostrar la lista completa de candidatos y sus votos, encontrar al 
candidato ganador (con más votos) y calcular el porcentaje de votos que 
obtuvo cada candidato. '''

#diccionario de empleados vacio
empleados = {}

continuar = True
while continuar:
    print("Seleccione una opción:")
    print("1. Agregar un nuevo empleado")
    print("2. Actualizar el salario de un empleado")
    print("3. Mostrar la lista completa de empleados")
    print("4. Calcular el promedio salarial por departamento")
    print("5. Salir")
    opcion = input("Ingrese el número de la opción que desea realizar: ")

    #agregar un nuevo empleado
    if opcion == "1":
        nombre = input("Ingrese el nombre del empleado: ")
        salario = float(input("Ingrese el salario del empleado: "))
        departamento = input("Ingrese el departamento al que pertenece el empleado: ")
        empleados[nombre] = {
            "salario": salario, 
            "departamento": departamento
            }
        print(f"Empleado {nombre} agregado con éxito.")
        print(empleados)

    #actualizar el salario de un empleado
    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado al que desea actualizar el salario: ")
        #si el empleado existe
        if nombre in empleados:
            salario = float(input("Ingrese el nuevo salario del empleado: "))
            empleados[nombre]["salario"] = salario
            print(f"Salario del empleado {nombre} actualizado con éxito.")
        else:
        #si el empleado no existe
            print(f"El empleado {nombre} no existe.")
        print(empleados)

    #mostrar la lista completa de empleados
    elif opcion == "3":
        print("Lista completa de empleados:")
        for nombre, empleado in empleados.items():
            print(f"Nombre: {nombre}, Salario: {empleado['salario']}, Departamento: {empleado['departamento']}")

    #calcular el promedio salarial por departamento
    elif opcion == "4":
        #pedir al usuario el departamento para el que desea calcular el promedio salarial
        departamento = input("Ingrese el departamento para el que desea calcular el promedio salarial: ")

        #inicializamos variables
        total_salarios = 0
        contador = 0
        # recorremos datos de los empleados guardados en los valores del diccionario
        for dato_empleado in empleados.values():
            if dato_empleado["departamento"] == departamento:
                total_salarios += dato_empleado["salario"]
                contador += 1

        #si hay empleados en el departamento
        if contador > 0:
            promedio = total_salarios / contador
            print(f"Promedio salarial para el departamento {departamento}: {promedio}")
        else:
            print(f"No hay empleados en el departamento {departamento}.")

    # calcular el promedio salarial por departamento de todos los departamentos
    #    departamentos = {}
    #    for nombre, empleado in empleados.items():
    #       if empleado["departamento"] in departamentos:
    #            departamentos[empleado["departamento"]].append(empleado["salario"])
    #        else:
    #            departamentos[empleado["departamento"]] = [empleado["salario"]]
    #    print("Promedio salarial por departamento:")
    #    for departamento, salarios in departamentos.items():
    #        promedio = sum(salarios) / len(salarios)
    #        print(f"Departamento: {departamento}, Promedio salarial: {promedio}")       
    #salir        
    elif opcion == "5":
        print("Saliendo del programa.")
        continuar = False
    else:
        print("Opción no válida. Intente de nuevo.")
        print("")