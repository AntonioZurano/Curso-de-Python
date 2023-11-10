# --- Pedir por pantalla los datos de un alumno 
#chico/chica
genero = input("Ingrese tu genero (chico/chica): ")
#nombre
nombre = input("Ingrese tu nombre: ")
nombres_chicas_A ="EHIJKLM"
nombre_chicos_A = "ABCDEFGHRSTUVWXYZ"

# --- Elegir grupo que corresponde --- #
# chica
if genero.lower() == "chica":
    if nombre[0].upper() in nombres_chicas_A:
        ## E hasta la M --> grupo A
        print("Tu grupo es A")
    else:
        ## el resto --> grupo B
        print("Tu grupo es B")    

# chico
elif genero.lower() == "chico":
    if nombre[0].upper() in nombre_chicos_A:
        ## A hasta la H, R hasta Z --> grupo A
        print("Tu grupo es A")
    else:
        ## el  resto --> grupo B
        print("Tu grupo es B")
        
# genero invalido
else:
    print("Genero invalido")
    exit()

