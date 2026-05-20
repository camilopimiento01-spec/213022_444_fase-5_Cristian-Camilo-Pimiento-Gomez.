#nombre del estudiante: Cristian Camilo Pimiento Gomez
#Grupo: 213022_444
# programa ingenieria electronica
#ejercicio 3

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    
    if stock_actual < stock_minimo:
        # Si el stock actual es menor al mínimo, se pide la diferencia
        return stock_minimo - stock_actual
    else:
        # Si hay suficiente stock, la cantidad a pedir es cero
        return 0

def ejecutar_auditoria():
    # Matriz con 5 artículos: [Código, Nombre, Stock Actual, Stock Mínimo]
    inventario = [
        ["A001", "Cables usb tipo v8", 15, 50],
        ["A002", "cable usb para iphone", 8, 5],
        ["A003", "cargador tipo v8", 3, 10],
        ["A004", "cargador tipo c", 12, 12],
        ["A005", "cable usb tipo c", 4, 20]
    ]
    
    print("=" * 55)
    print("      REPORTE DE AUDITORÍA Y ORDEN DE PEDIDO")
    print("=" * 55)
    print(f"{'Artículo':<30} | {'Cantidad a Pedir':<15}")
    print("-" * 55)
    
    # Recorremos la matriz fila por fila
    for articulo in inventario:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # Salida: Imprimir el nombre y la cantidad exacta calculada
        print(f"{nombre:<30} | {cantidad_pedir:<15}")
        
    print("=" * 55)

# Ejecutar el programa principal
if __name__ == "__main__":
    ejecutar_auditoria()