'''
REGISTRO DE VENTAS
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
de tus productos. Cada producto tiene un nombre y una cantidad
vendida. Implementa un programa en Python que utilice un diccionario
para almacenar la información de las ventas. El programa debe permitir
registrar las ventas de productos, actualizar la cantidad vendida de un
producto existente y calcular el total de ventas diarias.
(Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada
producto)'''

#diccionario de ventas vacio
ventas = {}
continuar = True
while continuar:
    opcion = input("1. Registrar ventas\n2. Actualizar cantidad vendida\n3. Calcular total de ventas diarias\n4. Salir\n")
    # Registrar ventas
    if opcion == "1":
        # Ingresar producto y cantidad vendida
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad vendida: "))
        # Si el producto ya esta registrado
        if producto in ventas:
            ventas[producto] += cantidad 
        # Si el producto no esta registrado    
        else:   
            ventas[producto] = cantidad
    # Actualizar cantidad vendida
    elif opcion == "2":
        # Ingresar producto y cantidad
        producto = input("Ingrese el nombre del producto: ")
        # Si el producto ya esta registrado
        if producto in ventas:
            # Pedimos la cantidad vendida de ese producto
            nueva_cantidad = int(input("Ingrese la nueva cantidad vendida: "))
            # Actualizamos la cantidad vendida de ese producto
            ventas[producto] = nueva_cantidad
        # Si el producto no esta registrado
        else:
            print("El producto no esta registrado")        
    # Calcular total de ventas diarias 
    elif opcion == "3":
        # Calcular total de ventas diarias de los valores del diccionario
        total = sum(ventas.values())
        # Imprimimos el total de ventas diarias
        print(f"El total de ventas diarias es: {total}")
    # Salir del programa
    elif opcion == "4":
        print("Saliendo del programa...")
        continuar=False        
    else:
        # si el numero no es valido, se imprime un mensaje de error
        print("Opción inválida. Por favor,  elije una opción válida.")