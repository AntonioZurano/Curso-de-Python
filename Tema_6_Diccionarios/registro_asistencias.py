'''
Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
una lista de fechas en las que asistió a clases. Implementa un programa
en Python que utilice un diccionario para almacenar la información de las
asistencias. El programa debe permitir registrar la asistencia de los
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
estudiantes y las fechas en las que asistieron.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de listas)
'''

#diccionario de asistencias vacio
asistencias = dict()
print(type(asistencias))

#Registrar la asistencia de los estudiantes
asistencias["Estudiante1"] = ["2021-01-01", "2021-01-05", "2021-01-10"]
asistencias["Estudiante2"] = ["2021-01-02", "2021-01-06", "2021-01-11"]
asistencias["Estudiante3"] = ["2021-01-03", "2021-01-07", "2021-01-12"]

print(asistencias)

#Agregar nuevas fechas de asistencia
asistencias["Estudiante1"].append("2021-01-15")
asistencias["Estudiante2"].append("2021-01-16")
asistencias["Estudiante3"].append("2021-01-17")

#Mostrar la lista de estudiantes y las fechas en las que asistieron
print("Registro de asistencias")
for estudiante, fechas in asistencias.items():
    print(f"Estudiante: {estudiante}")
    print("Fechas de asistencia:", " ".join(fechas))
    print("")
'''
#Otra forma
for estudiante in asistencias:
    print(f"Estudiante: {estudiante}")
    print(f"Fechas de asistencia: {asistencias[estudiante]}")
    print("")

#Otra forma
for estudiante, fechas in asistencias.items():
    print(f"Estudiante: {estudiante}")
    for fecha in fechas:
        print(fecha)
    print("")

#Otra forma

for estudiante, fechas in asistencias.items():
    print(f"Estudiante: {estudiante}")
    for i in range(len(fechas)):
        print(fechas[i])
    print("")
'''
