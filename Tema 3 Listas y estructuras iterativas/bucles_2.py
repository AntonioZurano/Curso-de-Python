''' Escribir un programa que almacene la cadena de caracteres
contraseña en una variable, pregunte al usuario por la contraseña
hasta que introduzca la contraseña correcta. '''

# --- pedir al usuario
password ="secreto"
password_entrada =""
password = input("Introduzca la contraseña: ")

# --- bucle para pedir la contraseña
# output: contraseña correcta
while password_entrada != password:
    password_entrada = input("Introduzca la contraseña: ")
    if password_entrada != password:
        print("Contraseña incorrecta. Intentelo de nuevo.")
print("Contraseña correcta. Acceso permitido.")

