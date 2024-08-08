''' Escribir un programa que almacene la cadena de caracteres
contraseña en una variable, pregunte al usuario por la contraseña
hasta que introduzca la contraseña correcta. '''

password = "secreto"

while True:
    password_entrada = input("Introduzca la contraseña: ")
    if password_entrada == password:
        print("Contraseña correcta. Acceso permitido.")
        break
    else:
        print("Contraseña incorrecta. Intentelo de nuevo.")