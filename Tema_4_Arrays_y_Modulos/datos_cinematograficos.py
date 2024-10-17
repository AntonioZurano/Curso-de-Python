# importar modulos
import numpy as np

# Crear un array con datos de ejemplo: pelicula, año, director y genero

peliculas = np.array([
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 120, 1990, 8.5],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]   
])

# ----- genero mas popular ------
# obtener los generos y apariciones en la base de datos
generos, conteos = np.unique(peliculas[:,1], return_counts=True)

# ordenar los conteos de mayor a menor
conteos_desc = np.argsort(conteos)[::-1] # nos devuelve los indices del array conteos ordenado de mayor a menor
print(conteos_desc)

# extraer el genero mas popular
genero_mas_popular = generos[conteos_desc[0]] # conteos_desc[0] es el indice con el conteo mas alto

print(f"El genero más popular es: {genero_mas_popular}")

# ----- agrupamos las peliculas por decada ------
print(peliculas[:,3])


#creamos array con las decadas a tratar
#decadas = (peliculas[:,3]//10)*10
decadas = np.unique(peliculas[:,3].astype(int) // 10 * 10) # convertir a entero y obtener las decadas redondeando y despues multiplicar por 10
# contamos las peliculas en cada decada
conteos_decadas = []
for decada in decadas:
    conteo = np.count_nonzero((peliculas[:,3].astype(int) >= decada) & (peliculas[:,3].astype(int) < decada + 10))
    conteos_decadas.append(conteo)

    print("En al decada de", decada, "se crearon", conteo, "peliculas")



# ----- duracion promedio por genero ------
todos_generos = peliculas[:,1]
duraciones = peliculas[:,2]
# inicializar array para guardar la duracion media
duracion_media = np.zeros(len(generos))

# duracion media
for i in range(len(generos)):
    duracion_media[i] = np.mean(duraciones[todos_generos == generos[i]].astype(float))
    print("Duracion media de las peliculas de tipo:", generos[i], "es de", duracion_media[i], "minutos")

