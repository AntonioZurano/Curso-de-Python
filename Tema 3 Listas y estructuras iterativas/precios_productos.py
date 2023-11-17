'''
Análisis de precios de productos:

Escribir un programa en Python que analice la lista
de precios de productos y determine el precio
más alto, el precio más bajo y el precio promedio
de todos los productos. Soluciona el ejercicio sin
usar las funciones max(), min() y sum().
'''

# --- lista de precios
precios = [10.99, 16.99, 21.99, 25.99, 29.99, 34.99, 39.99, 44.99, 49.99, 54.99]
precio_total = 0
precio_max = 0.0
precio_min = float('inf')
# --- bucle para recorrer la lista de precios
for precio in precios: 
    # if statement
    ## comprobamos si el precios es mas alto que el anterior
    if precio > precio_max:
        precio_max = precio
    # if statement
    ## comprobamos si el precio es mas bajo que el anterior
    if precio > precio_min:
        precio_min = precio
    ## sumamos los valores de la lista
    precio_total += precio
#print(precio_max)
#print(precio_min)
#print(precio_total)

# --- calculamos el precio promedio
precio_promedio = precio_total/len(precios)

# --- imprimirlos por pantalla
print("El precio mas alto es",precio_max)
print("El precio mas bajo es",precio_min)
print("El precio promedio es",precio_promedio)

if precio_max == precio_min:
    print("Todos los precios son iguales")