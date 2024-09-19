'''
Supón ahora que tu input es un string como este: 
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n 
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ''’

'''

# base de datos (lista de listas con los datos de los alumnos)
base_datos = [["Alvaro", "Gomez", "87654327B", "64782", "1", "7.6", "5.4", "9.3"]]

# nos dan de input esta cadena con informacion de los alumnos
cadena_alumnos = "David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n \
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n \
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n"

# --- formatear datos de entrada

# convertir la cadena en una serie del listas diferentes para cada alumno
alumnos = cadena_alumnos.split('\n') # creamos una lista de tres strings, uno para cada alumno
for alumno in alumnos:  # recorremos todos los strings de la lista
    alumno = alumno.strip() # quitamos espacios en el string que sobren al comienzo y al final
    datos_alumno = alumno.split() # split separara la cadena en una lista de valores individuales

    if datos_alumno: # comprobamos que la lista tiene contenido 
                     # para librarnos de cualquier error de formato
                     # añadimos las listas a la base de datos
        base_datos.append(datos_alumno)