'''Supongamos que eres el propieatario de una tienda
en línea y tienes una lista de ventas de los últimos 
30 días. Quieres analizar las ventas por día de la 
semana para identificar los días de mayor venta.
'''

# lista con las ventas del mes
ventas = [120, 80, 140, 200, 75, 100, 180, 50, 120, 80, 140, 200, 75, 100, 180, 50, 120, 80, 140, 200, 75, 100, 180, 50, 120, 80, 140]
# lista con los dias de la semana
dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
# lista donde guardar las ventas por dia de la semana
ventas_totales = [0,0,0,0,0,0,0]
# recorrer la lista de ventas
dia_venta = 0
for venta in ventas:
    # sumar las ventas por dia de la semana
    ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
    # guardar las ventas por dia de la semana en la lista
    dia_venta = dia_venta + 1
    if dia_venta == 7:
        #cambiamos el valor al indice del lunes
        dia_venta = 0
    
## sumar para cada dia de la semana las ventas realizadas


## imprimir las ventas realizadas para cada día de la semana
for i in range(7):
    print('Las ventas del', dias_semana[i], 'son', ventas_totales[i])
## a lo largo de es mes
