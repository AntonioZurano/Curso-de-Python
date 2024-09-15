
''' Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un 
programa para realizar un seguimiento de los productos que has vendido y el valor total de las 
ventas. Supongamos que hay un total de 10 productos.  
Tú has vendido 5 de estos productos en las siguientes cantidades: 
Producto 1: 3 unidades 
Producto 2: 1 unidad 
Producto 5: 7 unidades 
Producto 6: 2 unidades 
Producto 9 : 4 unidades 
Los precios de cada uno de estos productos son como siguen: 
Producto 1: 30.0 EU  Producto 6: 44.0 EU  
Producto 2: 9.8 EU  Producto 7: 21.2 EU 
Producto 3: 42.5 EU  Producto 8: 53.2 EU 
Producto 4: 32.6 EU  Producto 9: 25.3 EU 
Producto 5: 71.5 EU  Producto 10: 57.8 EU 
Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima 
la cantidad total de ventas, el dinero facturado por producto y el dinero total. 
'''
# --- Lista de productos y precios
# + lista de unidades vendidas de cada producto

precio_productos = [30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
unidades_producto = [3, 1, 0, 0, 7, 2, 0, 0, 4, 0]
#facturacion_producto = []

# el numero total de unidades vendidas es la suma de las unidades
# vendidas de cada producto
total_ventas = sum(unidades_producto)

# --- Bucle que recorra los productos (precips + unidades vendidas)

dinero_total = 0
# recorrecmos cada uno de los productos
for i in range(0, len(precio_productos)):
    # el dinero obtenido por cada producto será el precio del mismo
    # multiplicado por la cantidad de unidades vendidas
    dinero_por_producto = precio_productos[i] * unidades_producto[i]
    ###facturacion_producto.append(dinero_por_producto)
    # sumamos el dinero obtenido por cada producto al dinero total
    dinero_total = dinero_total + dinero_por_producto
    print(f"El dinero facturado por el producto {i + 1} es: {dinero_por_producto} EU.")

# --- Imprimir resultados
print("El numero total de unidades vendidas es:", total_ventas)
print("El dinero total facturado es:", dinero_total)


# output:
# cantidad total de ventas
# el dinero facturado por producto
# el dinero total

