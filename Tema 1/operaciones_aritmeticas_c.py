# --- Pedir al usuario dos numeros enteros ---
num1 = int(input("Introduce un número entero: ")) # string
num2 = int(input("Introduce otro número entero: ")) # string

# Calcular el cociente y el resto de la division entera
cociente = num1 // num2
resto = num1 % num2

# Mostrar el resultado por pantalla
print("Los números de entrada son ", num1, " y ", num2, ".")
print("El cociente es: " + str(cociente))
print("El resto es: " + str(resto))


