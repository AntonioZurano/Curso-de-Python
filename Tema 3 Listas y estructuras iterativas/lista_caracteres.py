'''
'''
# 1. crear lista
frutas=["manzana", "pera", "platano", "naranja", "limon", "kiwi", "fresa", "melocoton", "sandia", "melon"]

# 2. Longitud de la lista
print("La lista tiene", len(frutas), "elementos")

# 3. Mostrar el elemento 3 de la lista
print("El primer elemento de la lista es", frutas[2])

# 4. Modificar el segundo elemento de la lista
frutas[1]="mora"
print("El segundo elemento de la lista es", frutas[1])

# 5. Mostrar el ultimo elemento de la lista
print("El ultimo elemento de la lista es", frutas[-1])

# 6. Mostrar el penultimo elemento de la lista
print("El penultimo elemento de la lista es", frutas[-2])

# 7. Añadir un elemento al final de la lista
frutas.append("mango")
print("El ultimo elemento de la lista es", frutas[-1])

# 8. Añadir uva al comienzo de la lista
frutas.insert(0,"uva")

# 9. Eliminar el elemento 5 de la lista
frutas.pop(4)

# 10. Eliminar el elemento "pera" de la lista
frutas.remove("kiwi")

# 11. Mostrar la lista
print(frutas)

# 12. Mostrar la lista ordenada
frutas.sort()
print(frutas)

# 13. Mostrar la lista ordenada inversa
frutas.reverse()
print(frutas)

# 14. Recorrer la lista y mostrar cada elemento
for i in range(0,len(frutas)):
    print(frutas[i])

# 15. Eliminar el ultimo elemento de la lista
ultima_fruta = frutas.pop()
print(ultima_fruta)

# 16. recorrer lista e imprimir frutas
for fruta in frutas:
    print(fruta)

# 17 Imprimir la longitud de cada nombre de fruta
for fruta in frutas:
    print(f"fruta {fruta}. Longitud {len(fruta)}")

# 18. Imprimir nombres de mas de 5 caracteres
for fruta in frutas:
    if len(fruta) > 5:
        print(fruta)

# 19. Borrar strin cereza
frutas.remove("cereza")
print(frutas)

# 20. Vaciar la lista con clear
frutas.clear()
print(frutas)
