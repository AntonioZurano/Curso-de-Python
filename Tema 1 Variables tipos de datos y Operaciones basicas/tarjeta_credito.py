# --- Pedir al usuario que ingrese su numero de tarjeta ---
num_tarjeta = input("Ingresa tu número de tarjeta: ") # tipo string

# 1234 5678 9012 3456

print ("**** **** ****  ", num_tarjeta[12:16])

#  ---- Determinar la longitud del numero de tarjeta ----
longitud = ( len(num_tarjeta) )
#print("*"*10)
print("*" * (longitud-4) + num_tarjeta[longitud-4:longitud])

