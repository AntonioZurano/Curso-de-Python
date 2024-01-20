'''
Crea un programa que imprima todos los numeros primos entre el 2 y el 100.
Un numero primo es un numero positivo que tiene exactamente dos divisores positivos distintos: el mismo y el 1.

'''

#Version 1. Bucle for

for num in range (2, 100): #num tomara valores de 2 al 100

    prime= True #suponemos que el numero es primo a no ser
                #que se compruebe lo contrario
    
    for i in range(2, num): #i tomara valores de 2 al num

        if (num % i == 0):  # comprobamos que num es divisible por algun numero
                            # entre 2 y num-1
            prime= False    # si la condicion se cumple entonces sabemos que

            break           # que no es un numero primo --> prime = False
                            # si comprobamos una vez que el numero es primo no necesitamos 
                            # buscar mas divisores del numero luego podemos usar break
                            # para salir del bucle for y acrotar el tiempo de ejecucion del programa
        
    if prime:            # si prime es True entonces el numero es primo
        print(num)          # imprimimos el numero

#Version 2. Bucle while
for num in range(2, 100): # num tomara valores de 2 al 100

    prime= True #suponemos que el numero es primo a no ser
                #que se compruebe lo contrario
    i=2 # i tomara valores de 2 al num
    while prime and i<num:  # el bucle terminara si se comprueba que prime = False
                            # o si i toma un valor = o mayor que num
        if (num % i == 0):  # comprobamos que num es divisible por algun numero
                            # entre 2 y num-1
            prime= False    # si la condicion se cumple entonces sabemos que

            
        i=i+1               # aumentamos el valor de i en 1 para comprobar si num es divisible

    if prime: # si el numero es primo lo imprimimos por pantalla
        print(num)

    # si no es primo simplemente no hacemos nada y pasamos al siguiente numero     
        
        