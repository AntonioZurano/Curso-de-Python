# --- Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# --- Si el divisor es cero el programa debe mostrar un error. --- #
n = float(input("Introduce un número: "))
m = float(input("Introduce otro número: "))

# --- Comprobar si el divisor es cero --- #
if m == 0:
#si es cero imprimimos un error
    print("¡ERROR! No se puede dividir por 0.")
else:
# Si no es cero realizamos la división y mostramos el resultado    
    division = n/m    
    print("El resultado de dividir", n, " entre", m, " = ", division)
#si es cero imprimimos un error


