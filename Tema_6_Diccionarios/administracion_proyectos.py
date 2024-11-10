'''
Eres un gerente de proyectos y necesitas un programa para administrar
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
una descripción y un responsable asignado. Implementa un programa en
Python que utilice un diccionario para almacenar la información de las
tareas. El programa debe permitir agregar nuevas tareas, asignar
responsables a las tareas existentes, actualizar las descripciones de las
tareas y mostrar la lista completa de tareas y responsables.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de diccionarios)
'''

#diccionario de tareas vacio
tareas = {}


#Agregar nuevas tareas
tareas["Tarea1"] = {"descripcion": "Hacer informe", "responsable": "Juan"}
tareas["Tarea2"] = {"descripcion": "Enviar correo", "responsable": "Maria"}
tareas["Tarea3"] = {"descripcion": "Revisar documentos", "responsable": "Pedro"}

#Asignar responsables a las tareas existentes
tareas["Tarea1"]["responsable"] = "Ana"

#Actualizar las descripciones de las tareas
tareas["Tarea2"]["descripcion"] = "Enviar correo urgente"

print(tareas)
#Mostrar la lista de tareas y responsables
for tarea, detalles in tareas.items():
    print(f"Tarea: {tarea}")
    print(f"Descripción: {detalles['descripcion']}")
    print(f"Responsable: {detalles['responsable']}")
    print("")
