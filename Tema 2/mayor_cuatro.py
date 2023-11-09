# --- Pedir NUMEROS al usuario y decir cual es el mayor de los cuatro --- #
# --- Pedimos los numeros al usuario --- #
numero1 = input("Introduce el primer número: ")
numero1 = int(numero1)
numero2 = input("Introduce el segundo número: ")
numero2 = int(numero2)
numero3 = input("Introduce el tercer número: ")
numero3 = int(numero3)
numero4 = input("Introduce el cuarto número: ")
numero4 = int(numero4)

# --- Comprobamos cual es el mayor --- #
if numero1 >= numero2 and numero1 >= numero3 and numero1 >= numero4:
    print("El número mayor es: ", numero1)
elif numero2 >= numero1 and numero2 >= numero3 and numero2 >= numero4:
    print("El número mayor es: ", numero2)
elif numero3 >= numero1 and numero3 >= numero2 and numero3 >= numero4:
    print("El número mayor es: ", numero3)
else:
    print("El número mayor es: ", numero4)


