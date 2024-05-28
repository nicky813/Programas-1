def matriz_triangular_superior(matriz):
    # Verifica si la matriz es cuadrada
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada.")

    # Crea una copia de la matriz para no modificar la matriz original
    triangular_superior = [fila[:] for fila in matriz]

    # Itera sobre cada fila de la matriz
    for i in range(len(matriz)):
        # Itera sobre los elementos por debajo de la diagonal principal
        for j in range(i):
            # Establece los elementos por debajo de la diagonal principal a cero
            triangular_superior[i][j] = 0

    return triangular_superior

# Ejemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprime la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Llama a la función para obtener la matriz triangular superior
triangular_superior = matriz_triangular_superior(matriz)

# Imprime la matriz triangular superior
print("\nMatriz triangular superior:")
for fila in triangular_superior:
    print(fila)
