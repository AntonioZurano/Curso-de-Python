# importar modulos
import numpy as np

# Calificaciones de los estudiantes / input
calificaciones = np.array([
    [8, 7, 9, 10, 6],
    [10, 9, 8, 7, 6],
    [6, 8, 7, 9, 10],
    [7, 6, 8, 10, 9],
    [9, 10, 6, 8, 7]  
])

# Calcular la nota final de cada estudiante
examen1 = calificaciones[:, 0] # columna 0 examen 1
examen2 = calificaciones[:, 1]  # columna 1 examen 2
trabajo_final = calificaciones[:, 2] # columna 2 trabajo final
participacion = calificaciones[:, 3] # columna 3 participacion

# Calcular la nota final de cada estudiante
nota_final  = 0.3 * examen1 + 0.2 * examen2 + 0.3 * trabajo_final + 0.2 * participacion

# Imprimir la nota final de cada estudiante
for i in range(len(nota_final)):
    print(f"Estudiante {i+1} es: {nota_final[i]}")


