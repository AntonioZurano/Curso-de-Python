# --- Pedir un numero al usuario y decir si es par o impar --- #
numero = input("Introduce un número: ")
numero = int(numero)

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
