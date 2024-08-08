'''
Trabajas en un colegio y estas encargado de mantener un seguimiento de las notas de los estudiantes de una clase.
En tu base de datos tienes una lista con los nombres de los estudiantes, y para cada estudiante debes guardar sus notas
provenientes de deberes, exámenes y proyectos.
También necesitas calcular la nota media de cada estudiante y la nota media de la clase al completo.


Pista: Para resolver este problema, puedes usar una lista anidada donde guardes las notas para cada estudiante. Entonces
puedes usar un bucle para recorrer la lista y 
'''

# lista de estudiantes
estudiantes = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis']
# lista de notas de los estudiantes
database = []

# Función para añadir las notas de los estudiantes
for estudiante in estudiantes:
    # lista de notas de cada estudiante
    notas = []
    print("Introduce las notas de",estudiante)
    # lista de notas de cada estudiante
    # pido la nota de deberes, examen y proyectos
    deberes= float(input("Introduce la nota de deberes: "))
    notas.append(deberes)
    examen= float(input("Introduce la nota del examen: "))  
    notas.append(examen)    
    proyecto= float(input("Introduce la nota del proyecto: "))
    notas.append(proyecto)
    # añadimos las notas a la lista de notas
    database.append([estudiante,notas])

print(" ")
print(" ")
print(" ")
print("Calculando medias individuales y de la clase ")
print(" ")
print(" ")
print(" ")

# Función para calcular la nota media de un estudiante
for data in database:
    #extraemos el nombre del estudiante
    nombre=data[0]
    #extraemos las notas del estudiante
    notas=data[1]
    #calculamos la nota media del estudiante
    media=sum(notas)/len(notas)
    print(nombre, notas)
    #print("La nota media de",nombre,"es",media)
    print(f"La media de {nombre} es {media :.2f}") # :.2f para que solo muestre 2 decimales

# Función para calcular la nota media de la clase
notas_clase=[]
for data in database:
    notas_clase.append(data[1])
#print(notas_clase)
notas_clase=sum(notas_clase,[]) #convierte la lista de listas en una lista
print(notas_clase)
media_clase=sum(notas_clase)/len(notas_clase)
print("La media de la clase es {:.2f}".format(media_clase)) # :.2f para que solo muestre 2 decimales


