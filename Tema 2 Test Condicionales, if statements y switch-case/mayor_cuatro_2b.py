# --- Pedir NUMEROS al usuario y decir cual es el mayor de los cuatro --- #
# --- Pedimos los numeros al usuario --- #
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))
d = float(input("Introduce el cuarto número: "))

# --- Comprobamos cual es el mayor --- #
if (a>b):
  a, b = b , a

if (b>c):    
   b, c = c , b

if (c>d):
  c, d = d , c

print("El mayor de los cuatro es: ", d)
print("El orden de los números de menor a mayor es: ", a, b, c, d)


