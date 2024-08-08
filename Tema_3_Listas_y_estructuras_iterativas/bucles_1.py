# --- pedir al usuario
num = int(input("Introduzca la anchura central (numero entero): "))
# --- bucle ascendente
for i in range(num):
    print("*" *i + " " * (num-i))
# --- bucle descendente
for i in range(num-1,0,-1):
    print("*" * i + " " * (num-i))