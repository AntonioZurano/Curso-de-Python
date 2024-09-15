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
#recorrer la lista de usuarios y contraseñas
for i in range(len(nombres_usuario)):
    # comprobar si el usuario y la contraseña son correctos
    credenciales= False
    if usuario == nombres_usuario[i] and pasword == passwords[i]:
        credenciales = True

# imprimir mensaje de bienvenida o error
if credenciales == True:
    ### si son iguales damos bienvenida
    print('Bienvenido al sistema')
else:
    ### si no son iguales damos error
    print('Credenciales incorrectas')




