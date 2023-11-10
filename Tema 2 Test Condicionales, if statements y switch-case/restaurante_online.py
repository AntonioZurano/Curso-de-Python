# --- Pedir al usuario el tipo de hamburguesa
hamburguesa = input("Que hamburguesa desea? (clasica/vegana): ")



# --- Comprobamos que hamburguesa ha elegido el usuario --- #
# Si ha elegido la clasica
if hamburguesa.lower() == "clasica":
    ## Ofrecemos la opción de elegir un ingrediente extra: queso, bacon o huevo
    ingredientes_extra = input("Los ingredientes extra disponibles son: Queso \
                              Bacon, Huevo. Que ingrediente extra desea? queso/bacon/huevo): ")
## Imprimiremos que tipo de hamburguesa ha elegido y si ha elegido un ingrediente extra
    if ingredientes_extra.lower == "queso":
        print("Ha elegido la hamburguesa clasica con queso")
    elif ingredientes_extra.lower == "bacon":
        print("Ha elegido la hamburguesa clasica con bacon")
    elif ingredientes_extra.lower == "huevo":
        print("Ha elegido la hamburguesa clasica con huevo")
    else:
        print("El ingrediente extra no esta disponible")
    # Si ha elegido la vegana
elif hamburguesa.lower() == "vegana":
    ## Ofrecemos la opción de elegir un ingrediente extra: Tofu, Cebolla caramelizada
    ingredientes_extra = input("Los ingredientes extra disponibles son: Tofu, \
                                Cebolla caramelizada. Que ingrediente extra desea? tofu/cebolla caramelizada): ")
 ## Imprimiremos que tipo de hamburguesa ha elegido y si ha elegido un ingrediente extra
    if ingredientes_extra.lower() == "tofu":
        print("Ha elegido la hamburguesa vegana con tofu")
    elif ingredientes_extra.lower() == "cebolla caramelizada":
        print("Ha elegido la hamburguesa vegana con cebolla caramelizada")
    else:
        print("El ingrediente extra no esta disponible")
   
    ## Imprimimos un mensaje de error
else:
    print("La hamburguesa no esta disponible")
    exit()
