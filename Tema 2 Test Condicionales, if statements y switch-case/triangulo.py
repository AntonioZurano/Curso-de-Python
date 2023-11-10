# --- Pedir al usuario 3 longitudes de lados de un triangulo --- #
longitud1= float(input("Ingresa la primera longitud: "))
longitud2= float(input("Ingresa la segunda longitud: "))
longitud3= float(input("Ingresa la tercera longitud: "))
                 
# --- Comprobar si pueden conformar un triangulo --- #
if (longitud1 + longitud2 > longitud3) and (longitud2 + longitud3 > longitud1) and (longitud1 + longitud3 > longitud2):
    print("Con las piezas puedes formar un triangulo.")
else:
    print("Con las piezas no puedes formar un triangulo.")

# --- longitud1 + longitud2 > longitud3 --- #
# --- longitud2 + longitud3 > longitud1 --- #
# --- longitud1 + longitud3 > longitud2 --- #

