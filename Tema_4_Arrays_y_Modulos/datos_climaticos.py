# importar modulos
import numpy as np

import numpy as np

# Crear un array con datos de ejemplo: temperatura, humedad, presión y mes
climas = np.array([
    [15, 65, 1010, 1],
    [16, 68, 1011, 2],
    [17, 70, 1009, 2],
    [18, 72, 1008, 2],
    [20, 75, 1012, 3],
    [22, 78, 1011, 3],
    [25, 80, 1010, 4],
    [27, 82, 1009, 4],
    [30, 85, 1013, 4],
    [32, 88, 1015, 4],
    [35, 90, 1014, 5],
    [36, 89, 1013, 6],
    [34, 88, 1012, 7],
    [33, 86, 1010, 8],
    [31, 84, 1008, 8],
    [30, 83, 1007, 8],
    [28, 82, 1009, 9],
    [27, 81, 1010, 10],
    [24, 78, 1012, 10],
    [22, 76, 1013, 11],
    [18, 70, 1011, 12]
])

#print(climas)

# calcular la temperatura promedio por mes
meses = climas[:,3] # extraer el mes
temperaturas = climas[:,0] # extraer la temperatura
humedades = climas[:,1] # extraer la humedad
presiones = climas[:,2] # extraer la presion


temp_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)

# recorrer los valores para cada mes
for i in range(12):
    temp_mes[i] = np.mean(temperaturas[meses == i+1])
    humedad_mes[i]  = np.mean(humedades[meses == i+1])
    presion_mes[i]  = np.mean(presiones[meses == i+1])
    # imprimir la temperatura promedio por mes
    print(f"Temperatura promedio por mes: {i+1} fue de {temp_mes[i]:.2f} grados")
    # imprimir la humedad promedio por mes
    print(f"Humedad promedio por mes {i+1}: fue de {humedad_mes[i]:.2f} %")
    # imprimir la presion promedio por mes
    print(f"Presion promedio por mes {i+1}: fue de {presion_mes[i]:.2f} hPa")    

