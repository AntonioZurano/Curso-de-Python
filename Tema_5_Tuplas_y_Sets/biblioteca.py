''' Enunciado:
Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista 
de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del 
libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del 
libro y el apellido del autor. 
Pista: Tus datos de entrada podrían ser así  —> lista_libros = [(‘El aleph', ‘Jorge Luis 
Borges'), ('Cien años de soledad', ‘Garbriel Garcia Márquez'), ('La ciudad y los perros', 
‘Mario Vargas Llosa')]'''


# datos de entrada
lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Gabriel Garcia Marquez'), ('La ciudad y los perros', 'Mario Vargas Llosa')]
print("La lista de libros es:", tuple(lista_libros))
# Output: lista de tuplas --- titulo del libro, apellido del autor
titulos_y_apellidos = []
for titulo, autor in lista_libros:
    apellido = autor.split()[-1] # Obtenemos el apellido del autor separando el nombre completo por espacios y tomando el ultimo elemento
    titulos_y_apellidos.append((titulo, apellido))

print("Lista de libros con apellidos de autores es: ", tuple(titulos_y_apellidos)) # Devolvemos una tupla de tuplas
