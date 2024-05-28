def intercambiar_diagonales(matriz):
    # Verifica si la matriz es cuadrada
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada para intercambiar las diagonales.")

    # Itera sobre cada fila de la matriz
    for i in range(len(matriz)):
        # Intercambia los elementos de la diagonal principal y la diagonal secundaria
        matriz[i][i], matriz[i][len(matriz) - 1 - i] = matriz[i][len(matriz) - 1 - i], matriz[i][i]

    return matriz

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

# Llama a la función para intercambiar las diagonales
matriz_intercambiada = intercambiar_diagonales(matriz)

# Imprime la matriz con diagonales intercambiadas
print("\nMatriz con diagonales intercambiadas:")
for fila in matriz_intercambiada:
    print(fila)
