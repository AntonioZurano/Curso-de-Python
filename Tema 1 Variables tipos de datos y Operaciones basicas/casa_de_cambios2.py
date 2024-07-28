# --- Pedir al usuario que ingrese la cantidad en euros ---
euros = input("Ingresa la cantidad en euros que deseas convertir: ") # tipo string

# --- Convertimos la cantidad de euros a float ---
euros = float(euros)

# --- Convertir la cantidad de euros a dolares ---
dolares = euros * 1.2 

# --- Calculamos la cantidad que se queda la casa de cambios ---
tasas_gestion = dolares * 0.1

# --- Calculamos la cantidad de dolares que recibe el usuario ---
dolares_recibidos = dolares - tasas_gestion

# --- Imprimir la cantidad de dolares por pantalla ---
print("Monto ingresado: ", euros, "euros")
print("Cambio en dólares: ", dolares, "dólares")
print("Tasas de gestión: ", tasas_gestion, "dólares")
print("Monto a recibir: ", dolares_recibidos, "dólares")