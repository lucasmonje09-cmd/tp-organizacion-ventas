
import csv

ventas_por_producto = {}
ingresos_totales = 0

# Usamos rutas relativas como exige la consigna
with open('../datos/ventas.csv', mode='r') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        producto = fila['producto']
        cantidad = int(fila['cantidad vendida'])
        precio = float(fila['precio'])
        
        # Calcular totales
        ingresos_totales += (cantidad * precio)
        
        # Lógica de acumulación con diccionarios
        if producto in ventas_por_producto:
            ventas_por_producto[producto] += cantidad
        else:
            ventas_por_producto[producto] = cantidad

# Buscar el producto más vendido
producto_top = max(ventas_por_producto, key=ventas_por_producto.get)

# Guardar los resultados en la carpeta /resultados
with open('../resultados/informe_ventas.txt', 'w') as f:
    f.write("=== REPORTE DE VENTAS ===\n")
    f.write(f"Ingresos Totales: ${ingresos_totales}\n")
    f.write(f"Producto mas vendido: {producto_top} con {ventas_por_producto[producto_top]} unidades.\n")
