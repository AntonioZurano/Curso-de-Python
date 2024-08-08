# ---- Tenemos la contraseña correcta
key ="micontraseña123"

# --- Pedimos la contraseña al usuario --- #
password= input("Introduce la contraseña: ")

# --- Comprobamos si la contraseña es correcta --- #
if password == key:
    # --- Si coincide damos un la bienvenida --- #
    print("Contraseña correcta. ¡Bienvenido!")
else:
    # Si no coincide mostramos un error y pedimos la contraseña de nuevo--- #
    print("Error, la contraseña no es correcta.")   
    # --- Pedimos la contraseña al usuario --- #
    password= input("Introduce la contraseña: ")
    if password == key:
        ## si esta vez la contraseña coincide damos la bienvenida
        print("Contraseña correcta. ¡Bienvenido!")
    else:
        ## si no damos un mensaje de error y termina el programa
        print("Error, la contraseña no es correcta. Demasiados intentos.")
        print("Programa terminado.")





