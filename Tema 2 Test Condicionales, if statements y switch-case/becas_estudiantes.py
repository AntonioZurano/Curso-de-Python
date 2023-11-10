'''
EJERCICIOS 2A
BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes
con un mínimo de un 8 de media. Además, para acceder a la beca el 
estudiante debe tener entre 17 y 21 años. Crea un script que pida 
el nombre, la edad y la nota media del estudiante e indique si puede
optar a la beca o no. 
'''
# --- Pedir datos al usuario --- #
# nombre
nombre = input("Ingrese su nombre: ")
# edad
edad = int(input("Ingrese su edad: "))
# nota media
nota_media = float(input("Ingrese su nota media: "))
# --- Comprobar si puede optar a la beca --- #
# Comprobar si la nota media es mayor o igual a 8 y la edad esta entre 17 y 21
if nota_media >= 8 and 17 <= edad <= 21:
    print("Puede optar a la beca")
else:
    print("No puede optar a la beca")

    