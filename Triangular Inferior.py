def matriz_triangular_inferior(matriz):
    # Verifica si la matriz es cuadrada
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada.")

    # Crea una copia de la matriz para no modificar la matriz original
    triangular_inferior = [fila[:] for fila in matriz]

    # Itera sobre cada fila de la matriz
    for i in range(len(matriz)):
        # Itera sobre los elementos por encima de la diagonal principal
        for j in range(i + 1, len(matriz)):
            # Establece los elementos por encima de la diagonal principal a cero
            triangular_inferior[i][j] = 0

    return triangular_inferior

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

# Llama a la función para obtener la matriz triangular inferior
triangular_inferior = matriz_triangular_inferior(matriz)

# Imprime la matriz triangular inferior
print("\nMatriz triangular inferior:")
for fila in triangular_inferior:
    print(fila)
