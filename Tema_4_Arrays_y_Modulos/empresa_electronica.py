# importar modulos
import numpy as np

# datos de entrada
datos = np.array([['2022-01-01', 'Componente 1', 'Lote A', 80],
                 ['2022-01-15', 'Componente 1', 'Lote B', 90],
                 ['2022-02-01', 'Componente 2', 'Lote C', 85],
                 ['2022-02-15', 'Componente 2', 'Lote D', 95],
                 ['2022-03-01', 'Componente 1', 'Lote E', 75],
                 ['2022-03-15', 'Componente 2', 'Lote F', 90]])

# identificar el componente con la puntuacion mas alta
tipos_componente = datos[:, 1]
tipos_unicos = np.unique(tipos_componente)
print(tipos_unicos)
print(tipos_componente)
calidad = datos[:, 3].astype(float)
promedios = np.zeros(len(tipos_unicos))

i = 0
for tipo in tipos_unicos:
    #print(tipo)
    #print(calidad[tipos_componente == tipo])
    promedios[i] = np.mean(calidad[tipos_componente == tipo])
    i = i + 1

indice_maximo = np.argmax(promedios)
tipo_mejor_calidad = tipos_unicos[indice_maximo] 
print("El tipo de componente con la puntuacion de calidad mas alta es:", tipo_mejor_calidad)

# cuantos componentes se produjeron en cada mes
fechas = datos[:, 0]
meses, counts = np.unique([fecha[0:7] for fecha in fechas], return_counts=True)

for i in range(len(meses)):
    print("Mes:", meses[i], "Cantidad producida", counts[i])

# puntuacion de calidad promedio de cada uno de los componentes
promedio_por_tipo = np.zeros(len(tipos_unicos))
for i in range(len(tipos_unicos)):
    promedio_por_tipo[i] = np.mean(calidad[tipos_componente == tipos_unicos[i]])
    print("La puntuacion de calidad promedio para el", tipos_unicos[i], "es:", promedio_por_tipo[i])
