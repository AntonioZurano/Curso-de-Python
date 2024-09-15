'''
Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los 
últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor 
venta.  
Pista 1: Puedes crear dos listas, una con las ventas por cada día del mes como por ejemplo... 
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250] 
Y otra lista con los días de la semana: 
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", „Domingo“] 
Después puedes crear una nueva lista con una entrada por cada día de la semana y usar un bucle 
para añadir a esta lista la suma de las ventas correspondientes a cada uno de los días de la 
semana.  
Pista 2: Puede que necesites una variable que lleve la cuenta del día de la semana actual y se 
reinicie a cero cuando llegue al séptimo día.  
Pista 3: Puedes usar el operador módulo (%) para llevar la cuenta del día de la semana. 
'''

#lista con las ventas del mes
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
#lista con los dias de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
#lista para guardar las ventas por dia de la semana
ventas_semana = [0, 0, 0, 0, 0, 0, 0]
#variable para llevar la cuenta del dia de la semana
ventas_totales = [0, 0, 0, 0, 0, 0, 0]
#recorrer la lista de ventas con un bucle
dia_venta = 0
for venta in ventas:
    ## sumar para cada dia de la semana las ventas correspondientes
    ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
    dia_venta = dia_venta + 1
## sumar para cada dia de la semana las ventas correspondientes

## imprimir las ventas realizadas para cada dia de la semana
## a lo largo de ese mes