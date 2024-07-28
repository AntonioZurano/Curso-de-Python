#1 Escribe un programa que muestre por pantalla la cadena estas usando phyton
mensaje = "estas usando phyton"
print(mensaje)
#2 Amplia el programa anterior para que pida al usuario su nombre y lo muestre por pantalla junto con un mensaje de bienvenida.
nombre=""
#nombre= input()
nombre=input("Introduce tu nombre: ") # de tipo string
nombre = nombre.title()
#--- Reformatear nombre ---
nombre = nombre.replace(".", "")
#--- Reformatear nombre ---
lenguaje = 'python'
#--- Escribimos mensaje en una variable ---
print("¡Hola, " + nombre.title() +", estas usando ", lenguaje.title() + "!")
# --- imprimimos mensaje por pantalla ---
#3 Usa una función interna de python que actúe sobre el string que has creado
#antes y muestre por pantalla el mismo string pero con todas las letras en mayúsculas.
print(nombre.upper())
#4 Usa una función interna de python que actúe sobre el string que has creado
print(nombre.lower())
#--- Reformatear nombre ---
nombre = nombre.replace(".", "")



