'''
    Supongamos que eres un administrador de sistemas
    y necesitas validar el acceso de los usuarios a un
    sitio web. Crea un script que verifique si el
    nombre de usuario y la contraseña ingresados son correctos 
    y permita el acceso solo si ambos son correctos
'''


# lista de nombre de usuario
nombres_usuario = ['admin', 'usuario1', 'usuario2', 'usuario3']
# lista de contraseñas
passwords = ['admin', '1234', '1234', '1234']
# pedir al usuario que ingrese su nombre de usuario
usuario = input('Ingrese su nombre de usuario: ')
# pedir al usuario que ingrese su contraseña
pasword = input('Ingrese su contraseña: ')


# validar el acceso
credenciales = False
#recorrer la lista de usuarios y contraseñas
i = 0
while i < len(nombres_usuario):
   # comprobar si el usuario y la contraseña son correctos
    if usuario == nombres_usuario[i] and pasword == passwords[i]:
         credenciales = True
    i = i + 1     

# imprimir mensaje de bienvenida o error
if credenciales:
    print('Bienvenido, Acceso concedido')
    ## si no denegamos el acceso
else:
    print('Error, credenciales incorrectas')
    ## si son iguales damos bienvenida
    ## si no son iguales damos error



### si son iguales damos bienvenida
### si no son iguales damos error