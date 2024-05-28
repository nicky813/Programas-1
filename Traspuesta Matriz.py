def traspuesta(matriz):
    # Calcula las dimensiones de la matriz original
    filas_originales = len(matriz)
    columnas_originales = len(matriz[0])

    # Inicializa una matriz vacía para almacenar la traspuesta
    matriz_traspuesta = []

    # Itera sobre las columnas de la matriz original
    for j in range(columnas_originales):
        # Inicializa una lista vacía para almacenar una columna de la traspuesta
        columna_traspuesta = []
        # Itera sobre las filas de la matriz original
        for i in range(filas_originales):
            # Agrega el elemento correspondiente a la columna traspuesta
            columna_traspuesta.append(matriz[i][j])
        # Agrega la columna traspuesta a la matriz traspuesta
        matriz_traspuesta.append(columna_traspuesta)

    return matriz_traspuesta

# Ejemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcula la traspuesta de la matriz
matriz_traspuesta = traspuesta(matriz)

# Imprime la matriz original y su traspuesta
print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nTraspuesta de la matriz:")
for fila in matriz_traspuesta:
    print(fila)
