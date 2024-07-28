# Una compañia de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM todoterreno.
# Cada uno de estos coches tiene un precio de venta y el vendedor recibe una comisión diferente por cada uno de ellos.

# --- Preguntar al usuario cuantos coches ha vendido de cada tipo ---
rbm_serie1_vendidos = int(input("¿Cuántos coches RBM Serie 1 has vendido? "))
rbm_plus_vendidos = int(input("¿Cuántos coches RBM Serie plus has vendido? "))
rbm_todoterreno_vendidos = int(input("¿Cuántos coches RBM todoterreno has vendido? "))
# --- Guardar los datos en variables ---
precio_rbm_serie1 = 20000
precio_rbm_plus = 30000
precio_rbm_todoterreno = 40000

comision_rbm_serie1 = 0.05
comision_rbm_plus = 0.1
comision_rbm_todoterreno = 0.15

# --- Calculamos la cantidad de euros a comisionar ese mes ---
ganancia_rbm_serie_1 = rbm_serie1_vendidos * precio_rbm_serie1 * comision_rbm_serie1
ganancia_rbm_plus = rbm_plus_vendidos * precio_rbm_plus * comision_rbm_plus
ganancia_rbm_todoterreno = rbm_todoterreno_vendidos * precio_rbm_todoterreno * comision_rbm_todoterreno

print(ganancia_rbm_serie_1)
print(ganancia_rbm_plus)
print(ganancia_rbm_todoterreno)

ganancia_total = ganancia_rbm_serie_1 + ganancia_rbm_plus + ganancia_rbm_todoterreno

# --- Imprimir la cantidad de euros por pantalla ---
print("Este mes has ganado: ", ganancia_total, "euros")

