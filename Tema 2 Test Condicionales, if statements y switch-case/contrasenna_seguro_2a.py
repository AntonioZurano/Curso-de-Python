''' Por motivos de seguridad una contraseña debe tener
una vocal minúscula, dos símbolos especiales (+ o #) .
Dada una contraseña, ingresada por el usuario,
comprueba si es segura o no.'''


# Solicitar la contraseña al usuario
password = input("Introduce tu contraseña: ")

# Comprobar si tiene al menos una vocal minúscula
if ("a" in password or "e" in password or "i" in password or "o" in password or "u" in password) and ("*" in password or "#" in password):
     print("La contraseña es segura")
else:
    print("La constraseña no es segura")
# Si no los cumple diremos que es insegura