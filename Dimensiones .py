def dimensiones_matriz(matriz):
    # Verifica si la matriz está vacía
    if not matriz:
        return 0, 0  # Si la matriz está vacía, devuelve (0, 0) indicando que no hay filas ni columnas.
    
    # Calcula el número de filas
    filas = len(matriz)
    
    # Calcula el número de columnas (se asume que todas las filas tienen el mismo número de columnas)
    columnas = len(matriz[0])
    
    # Devuelve el número de filas y columnas como una tupla
    return filas, columnas

# Ejemplo de uso:
matriz_ejemplo = [
    [1, 2, 3],  # Primera fila
    [4, 5, 6],  # Segunda fila
    [7, 8, 9]   # Tercera fila
]

# Llama a la función para obtener las dimensiones de la matriz
filas, columnas = dimensiones_matriz(matriz_ejemplo)

# Imprime el resultado
print(f"La matriz tiene {filas} filas y {columnas} columnas.")
