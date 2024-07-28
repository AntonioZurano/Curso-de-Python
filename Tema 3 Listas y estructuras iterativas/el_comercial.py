'''
Eres un comercial trabajando para una compañia que vende diversos productos. Quieres crear un
programa para realizar un seguimiento de los productos que has vendido y el valor total de las 
ventas. Supongamos que hay un total de 10 productos.
'''

# --- lista de productos y precios
# + lista de unidades vendidas de cada producto
productos = ["camiseta", "pantalon", "calcetines", "gorra", "guantes", "bufanda", "chaqueta", "falda", "vestido", "zapatos"]
precio_productos = [10, 20, 5, 8, 15, 7, 25, 15, 30, 40]
unidades_producto = [3, 1, 0, 0, 7, 2, 0, 0, 4, 0]
facturacion_producto = []

total_ventas = sum(unidades_producto)
dinero_total= 0
# --- Bucle que recorra los productos (precios y unidades vendidas)
for i in range(0, len(precio_productos)):
    # + calcular el dinero facturado por producto
    dinero_por_producto = precio_productos[i] * unidades_producto[i]
    # + añadir el dinero facturado por producto a la lista de facturacion
    facturacion_producto.append(dinero_por_producto)
    # + calcular el dinero total facturado
    dinero_total = dinero_total + dinero_por_producto
    # --- Imprimir el resultado
    if unidades_producto[i] > 0:
        print("El producto", productos[i], "tiene un precio de", precio_productos[i], "y se han vendido", unidades_producto[i], "unidades")

# ---- Imprimir el resultado

# output:
# cantidad total de ventas
# el dinero facturado por producto
# el dinero total facturado
print("Cantidad total de ventas:", total_ventas)
print("Dinero facturado por producto:", facturacion_producto)
print("Dinero total facturado:", dinero_total)
