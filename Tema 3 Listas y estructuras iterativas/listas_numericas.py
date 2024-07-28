# --- Paso 1

#numeros = [1,2,3,4,5,6,7,8,9,10]

numeros = list(range(1,11))
print(numeros)

# --- Paso 2

pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)
pares_invertidos = pares[::-1]
print(pares_invertidos)

# --- Paso 3

for num in numeros:
    print(num**2)

# --- Paso 4
numeros_pares_invertidos = [numero for numero in numeros if numero % 2 == 0][::-1]
numeros_cuadrados = [numero**2 for numero in numeros]

print(numeros_pares_invertidos)
print(numeros_cuadrados)

# --- Paso 5
minimo = min(numeros)
print(minimo)

# --- Paso 6
maximo = max(numeros)   
print(maximo)

# --- Paso 7
# con bucle
suma = 0
for numero in numeros:
    suma += numero
print(suma)

# sin bucle
suma = sum(numeros)
print(suma)

# --- Paso 8
indice_8_original = numeros.index(8)
print(indice_8_original)

indice_8_invertido = numeros_pares_invertidos.index(8)
print(indice_8_invertido)