# Crea un script que pida los tiempos por pantalla para cada uno de los finalistas
# de una carrera de 100 metros lisos y muestre por pantalla el tiempo que ha tardado
# en recorrer la distancia el ganador de la carrera.

# --- Pedir al usuario que ingrese el tiempo del finalista 1 ---
tiempo_hannah = input("Ingresa el tiempo de Hannah Neis: (formato: minutos segundos centésimas): ") 
tiempo_jackie = input("Ingresa el tiempo de Jackie Narracott: (formato: minutos segundos centésimas): ")
tiempo_kimberly = input("Ingresa el tiempo de Kimberley Bos: (formato: minutos segundos centésimas): ")

# --- Extraer minutos, segundos y centésimas de Hannah Neis ---
minutos_hannah, segundos_hannah, centesimas_hannah = tiempo_hannah.split(" ")
minutos_jackie, segundos_jackie, centesimas_jackie = tiempo_jackie.split(" ")
minutos_kim, segundos_kim, centesimas_kim = tiempo_kimberly.split(" ")

# --- Convertimos los tiempos de Hannah Neis a float ---
tiempo_hannah = float(minutos_hannah) * 60 + float(segundos_hannah) + float(centesimas_hannah) * 0.01
tiempo_jackie = float(minutos_jackie) * 60 + float(segundos_jackie) + float(centesimas_jackie) * 0.01
tiempo_kimberly = float(minutos_kim) * 60 + float(segundos_kim) + float(centesimas_kim) * 0.01

# --- Imprimir los tiempos por pantalla ---
print("Hannah Neis ha tardado: ", tiempo_hannah, "segundos")
print("Jackie Narracott ha tardado: ", tiempo_jackie, "segundos")
print("Kimberley Bos ha tardado: ", tiempo_kimberly, "segundos")

# --- Calculamos la velocidad media ---
velocidad_media_hannah = 100 / tiempo_hannah
velocidad_media_jackie = 100 / tiempo_jackie
velocidad_media_kimberly = 100 / tiempo_kimberly

# --- Imprimir la velocidad media por pantalla ---
print("Hannah Neis ha recorrido la distancia a una velocidad media de: ", velocidad_media_hannah, "metros/segundo")
print("Jackie Narracott ha recorrido la distancia a una velocidad media de: ", velocidad_media_jackie, "metros/segundo")
print("Kimberley Bos ha recorrido la distancia a una velocidad media de: ", velocidad_media_kimberly, "metros/segundo")

