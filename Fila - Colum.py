def suma_filas_columnas(matriz):
    # Inicializa listas para almacenar las sumas de filas y columnas
    suma_filas = []
    suma_columnas = [0] * len(matriz[0])
    
    # Itera sobre cada fila de la matriz
    for fila in matriz:
        # Calcula la suma de la fila actual
        suma_fila = sum(fila)
        # Añade la suma de la fila a la lista de sumas de filas
        suma_filas.append(suma_fila)
        
        # Itera sobre cada elemento de la fila
        for i in range(len(fila)):
            # Añade el valor del elemento a la suma de la columna correspondiente
            suma_columnas[i] += fila[i]
    
    # Devuelve las listas de sumas de filas y columnas
    return suma_filas, suma_columnas

# Ejemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Llama a la función para encontrar las sumas de filas y columnas
suma_filas, suma_columnas = suma_filas_columnas(matriz)

# Imprime las sumas de las filas
print("Suma de las filas:", suma_filas)

# Imprime las sumas de las columnas
print("Suma de las columnas:", suma_columnas)
