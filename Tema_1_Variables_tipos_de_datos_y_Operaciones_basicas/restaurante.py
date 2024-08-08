# --- Definir el precio de cada alimento ---
precio_ensalada_mixta = 12
precio_sopa_pescado = 10
precio_dorada_horno = 18
precio_arroz_curry = 14
precio_lasagna_carne = 15
precio_brownie_chocolate = 8
precio_helado = 6
precio_refresco = 5.5
precio_cafe = 3.5

# --- Pedir al usuario que introduzca la cantidad de cada alimento que ha consumido ---
ensalada_mixta = input("¿Cuántas ensaladas mixtas has consumido? ")
sopa_pescado = input("¿Cuántas sopas de pescado has consumido? ")
dorada_horno = input("¿Cuántas doradas al horno has consumido? ")
arroz_curry = input("¿Cuántos arroces al curry has consumido? ")
lasagna_carne = input("¿Cuántas lasañas de carne has consumido? ")
brownie_chocolate = input("¿Cuántos brownies de chocolate has consumido? ")
helado = input("¿Cuántos helados has consumido? ")
refresco = input("¿Cuántos refrescos has consumido? ")
cafe = input("¿Cuántos cafés has consumido? ")

# --- Calculamos el total de la cuenta ---
total = ensalada_mixta * precio_ensalada_mixta + \
sopa_pescado * precio_sopa_pescado + \
dorada_horno * precio_dorada_horno + \
arroz_curry * precio_arroz_curry + \
lasagna_carne * precio_lasagna_carne + \
brownie_chocolate * precio_brownie_chocolate + \
helado * precio_helado + \
refresco * precio_refresco \
+ cafe * precio_cafe

# -- Imprimir el total de la cuenta por pantalla ---
print("El total de la cuenta es: ", total, "euros")
