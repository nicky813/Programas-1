def determinante_matriz_2x2(matriz):
    # Verifica si la matriz es de tamaño 2x2
    if len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
        raise ValueError("La matriz debe ser 2x2 para calcular su determinante.")

    # Calcula el determinante usando la fórmula
    determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    return determinante

# Ejemplo de uso:
matriz = [
    [1, 2],
    [3, 4]
]

# Calcula el determinante de la matriz
det = determinante_matriz_2x2(matriz)

# Imprime el resultado
print("El determinante de la matriz es:", det)
