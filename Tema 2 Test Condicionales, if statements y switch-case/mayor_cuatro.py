# --- Pedir NUMEROS al usuario y decir cual es el mayor de los cuatro --- #
# --- Pedimos los numeros al usuario --- #
a = input("Introduce el primer número: ")
a = float(a)
b = input("Introduce el segundo número: ")
b = float(b)
c = input("Introduce el tercer número: ")
c = float(c)
d = input("Introduce el cuarto número: ")
d = float(d)

# --- Comprobamos cual es el mayor --- #
if (a>b):
  a, b = b , a

if (b>c):    
   b, c = c , b

if (c>d):
  c, d = d , c
print("El mayor de los cuatro es: ", d)
print("El orden de los números de menor a mayor es: ", a, b, c, d)


