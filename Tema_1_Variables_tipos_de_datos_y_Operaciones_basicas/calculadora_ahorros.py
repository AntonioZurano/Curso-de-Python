# --- Pedir nombre de usuario ---
nombre = input("¿Cuál es tu nombre? ")
# --- Saludar al usuario ---
print("¡Hola, " + nombre + "!")

# --- Guardamos ingresos y horas trabajadas
ingresos_hora = float(input("¿Cuánto ganas por hora? ")) # en euros
#ingresos_hora = 25 # en euros
horas_trabajadas = float(input("¿Cuántas horas trabajas a la semana? ")) # en horas
#horas_trabajadas = 40 # en horas

# Calculamos la ganancia semanal
salario_semanal = ingresos_hora * horas_trabajadas

# Calculamos la ganancia anual
ganancia_anual = salario_semanal * 52

# Imprime ganancia anula por pantalla
print(nombre.title(), "tienes unas ganancias anuales de ", ganancia_anual, " euros.")

# --- Pedir al usuario los gastos semanales
gastos_semanales = float(input("Ingresas tus gastos semanales: "))

# --- Calcular el gasto anual
gasto_anual = gastos_semanales * 52

# --- Calcular el ahorro anual
ahorro_anual = ganancia_anual - gasto_anual

print(nombre.title(), "tienes un ahorro anual de ", ahorro_anual, " euros.")

