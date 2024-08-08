# --- Pedir un numero al usuario y decir si es par o impar --- #
numero = input("Introduce un número: ")
numero = int(numero)

# --- Comprobar si el número es par o impar
# si es un multiplo de 2 será par
if numero % 2 == 0:
    print("El número", numero, "es par.")
# si no será impar
else:
    print("El número", numero, "es impar.")
