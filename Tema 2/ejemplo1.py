''' Crea un script que dado un usuario le de 
una bienvenida personalizada si es el administrador
o una bienvenida general si es un usuario normal'''

# --- Pedir al usuario que introduzca su nombre
nombre = input("Introduce tu nombre: ")
# --- Nombre del administrador
administrador = "Alejandro"

# --- Comprobar si ese nombre es igual que el del administrador
# si es igual, le damos una bienvenida personalizada
if nombre.lower == administrador: # case insensitive
    print("Bienvenido, ", nombre.tittle(), "!")

# si no es igual, le damos una bienvenida general
else:    
    print("¡Bienvenido invitado!")


