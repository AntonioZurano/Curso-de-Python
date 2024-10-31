#Enunciado
'''Una red social tiene una base de datos de usuarios y sus correspondientes amistades. 
Crea un programa que tome una base de datos de una red social como una lista de 
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los 
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas 
diferentes. Deberas eliminar las cuentas duplicadas y después  devolver una tupla de 
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos. 
Pista 1: Tus datos de entrada podrían ser así  —>  red_social = [("Juan", ["Maria", "Pedro", 
"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])] 
Pista 2: Para eliminar duplicidades puedes usar sets'''

# datos de entrada
red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro","Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

# Eliminamos las cuentas duplicadas en amigos
#for i in range(len(red_social)):
    #usuario = red_social[i][0]
    #amigos = red_social[i][1]
red_social_sin_duplicados = []
for usuario, amigos in red_social:
    amigos_sin_duplicados = set(amigos) # Elimina duplicados al convertir en conjunto se eliminan los duplicados
    red_social_sin_duplicados.append((usuario, amigos_sin_duplicados))
    #amigos = list(set(amigos))
    #red_social[i] = (usuario, amigos)
print(tuple(red_social_sin_duplicados))

# Contar el numero de amigos de cada usuario
amigos_por_usuario = []
for usuario, amigos in red_social_sin_duplicados:
    amigos_por_usuario.append((usuario, len(amigos)))
    print(usuario, len(amigos))

# Output: tuplas de tuplas --- usuario, numero de amigos
print(tuple(amigos_por_usuario))

# Output: Usuario con mas amigos
max_amigos = max(amigos_por_usuario, key=lambda x: x[1])
