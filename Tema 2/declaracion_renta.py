# --- Pedir datos al usuario --- #
# edad
edad = int(input("Ingrese su edad: "))
# ingreso
ingreso = float(input("Ingrese su ingreso mensual en euros: "))
# --- Comprobar si se debe aplicar el tipo impositivo y comprobar cual --- #

#--- Comprobar si se debe aplicar el tipo impositivo --- #
# Comprobar si el usuario es mayor de edad y sus ingresos --> si debe tributar
if edad >= 18 and ingreso > 1000:
    print("Eres susceptible de tributar") 
## calcular su renta anual
    renta_anual = ingreso * 12
    print("Su renta anual es: " + str(renta_anual) + " euros")    
## comprobar en que tramo se encuentra su ingreso anual
    if renta_anual < 15000:
        print("Su tipo impositivo es del 5%")
    elif 15000 <=renta_anual < 25000:
        print("Su tipo impositivo es del 15%")
    elif 25000 <= renta_anual < 35000:
        print("Su tipo impositivo es del 20%")
    elif 35000 <= renta_anual < 60000:
        print("Su tipo impositivo es del 30%")
    else:
        print("Su tipo impositivo es del 45%")
## Si el usuario no esta en el rango de edad o ingresos
else:
    print("No tiene obligacion de tributar")
## imprimir que no tiene obligacion de tributar