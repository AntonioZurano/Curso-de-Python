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
ventas["Producto1"] = 10
ventas["Producto2"] = 5
ventas["Producto3"] = 3
ventas["Producto4"] = 8

#print(ventas)

#Actualizar cantidad vendida de un producto existente

ventas["Producto2"] = ventas["Producto2"] + 2
#otra forma de hacerlo
ventas["Producto2"] += 2

#print(ventas)

#Calcular el total de ventas diarias
total = 0
for producto, cantidad in ventas.items():
    total += cantidad

print(f"El total de ventas diarias es: {total}")

# otra forma de hacer
total = sum(ventas.values())
print(f"El total de ventas diarias es: {total}")

#Otra forma
total_ventas = 0
for cantidad in ventas.values():
    total_ventas += cantidad
print(f"El total de ventas diarias es: {total}")

#Imprimir el registro de ventas y el total de ventas diarias
for producto, cantidad in ventas.items():
    print(f"{producto}: {cantidad}")

print(f"El total de ventas diarias es: {total_ventas}")