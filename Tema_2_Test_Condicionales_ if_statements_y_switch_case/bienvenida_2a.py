''' Un ordenador tiene tres usuarios distintos (alejandro, 
Naomi y Sergio) y otro usuario invitado. Crea un script que
dado un usuario le de una bienvenida personalizada si es uno
de los tres usuarios o una bienvenida general si es el
usuario invitado'''


# --- Pedimos el nombre de usuario
nombre=input("Introduce tu nombre de usuario: ")
# --- Variables con nombres de los usuarios
# --- que pueden acceder al sistema
usuario_1="alejandro"
usuario_2="naomi"
usuario_3="sergio"
# --- Convertimos el nombre de usuario a minúsculas
# --- para que no haya problemas con las mayúsculas
# --- y minúsculas
nombre=nombre.lower()
# --- eliminamos los espacios en blanco que pueda tener
nombre=nombre.replace(" ","")
# --- eliminamos las comillas que pueda tener
nombre=nombre.replace("'","")
# --- eliminamos los puntos que pueda tener
nombre=nombre.replace(".","")
# --- Comprobamos si es uno de los tres usuarios
if nombre==usuario_1 or nombre==usuario_2 or nombre==usuario_3:
    # --- Si es uno de los tres usuarios damos la bienvenida personalizada
    print("Bienvenido "+nombre.title())

# --- Si es el usuario invitado damos la bienvenida general
elif nombre=="invitado":
    print("Bienvenido usuario invitado")
# --- Si no es ninguno de los anteriores damos un mensaje de error
else:
    print("Usuario no reconocido")
