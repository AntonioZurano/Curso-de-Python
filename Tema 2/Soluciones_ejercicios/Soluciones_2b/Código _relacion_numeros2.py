# --- Pedir tres numeros
x = float(input("Introduce el primer numero: "))
y = float(input("Introduce el segundo numero: "))
z = float(input("Introduce el tercer numero: "))

if x == y+z or y == x+z or z == x+y:
    print(True)
else:
    print(False)