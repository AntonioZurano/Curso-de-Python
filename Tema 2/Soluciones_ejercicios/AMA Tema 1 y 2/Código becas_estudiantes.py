'''
EJERCICIOS 2A
BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes 
con un mínimo de un 8 de media. Además para acceder a la beca el 
estudiante debe tener entre 17 y 21 años. Crea un script que pida
el nombre, la edad y la nota media del estudiante e indique si 
puede optar a la beca o no.
'''

# --- Pedir los datos al usuario
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
nota_media = float(input("Introduce tu nota media: "))


# -- Comprobar si cumple las condiciones
# nota media > 8 + edad 17 - 21
if nota_media >= 8 and 17 <= edad <=21:
    # Imprimiremos que la condicion la cumple
    print(nombre, "puede optar a la beca")
else:
    # si no imprimiremos que la condicion no se cumple
    print(nombre, "no puede acceder a la beca")

