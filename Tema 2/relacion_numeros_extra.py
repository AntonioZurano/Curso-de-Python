# Pedir al usuario 3 numeros diferentes
x = int(input("Introduce el primer número: "))
y = int(input("Introduce el segundo número: "))
z = int(input("Introduce el tercer número: "))

if x == y+z or y == x+z or z == x+y:
    print("True")   
else:
    print("False")