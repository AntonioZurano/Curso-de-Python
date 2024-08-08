# --- Pedimos un precio al usuario --- #
precio = float(input("Ingrese el precio en dolares: "))

# comprobar el precio y ver si debemos comprar, holdear o vender
if precio < 100:
    print("Es hora de comprar")
elif 100.0 <= precio <= 150:
    print("Toca holdear")
else:
    print("Es hora de vender")