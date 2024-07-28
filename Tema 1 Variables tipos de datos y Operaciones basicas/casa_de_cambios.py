# --- Pedir al usuario que ingrese la cantidad en euros ---
euros = input("Ingresa la cantidad en euros que deseas convertir: ") # tipo string

# --- Convertimos la cantidad de euros a float ---
euros = float(euros)

# --- Convertir la cantidad de euros a dolares ---
dolares = euros * 1.2 

# --- Imprimir la cantidad de dolares por pantalla ---
print(euros, "euros son" +  " dólares")
