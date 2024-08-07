
# Pedir al usuario 3 numeros diferentes
x = int(input("Introduce el primer número: "))
y = int(input("Introduce el segundo número: "))
z = int(input("Introduce el tercer número: "))

# Verificar si alguno de ellos es la suma de los otros dos
# Si es cierto imprimir True
# Si es falso imprimir False
if (x==y+z):
    print("El primer número es la suma de los otros dos.")
elif (y==x+z):
    print("El segundo número es la suma de los otros dos.")
elif (z==x+y):
    print("El tercer número es la suma de los otros dos.")
else:
    #Si es falso imprimir False
    print("Ninguno de los números es la suma de los otros dos.")


