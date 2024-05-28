def es_matriz_identidad(matriz):
    # Verifica si la matriz es cuadrada
    if len(matriz) != len(matriz[0]):
        return False

    # Itera sobre los elementos de la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # Verifica si los elementos fuera de la diagonal principal son cero
            if i != j and matriz[i][j] != 0:
                return False
            # Verifica si los elementos en la diagonal principal son uno
            if i == j and matriz[i][j] != 1:
                return False

    # Si pasa todas las verificaciones, la matriz es la matriz identidad
    return True

# Ejemplo de uso:
matriz_identidad = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

matriz_no_identidad = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 1]
]

# Verifica si la matriz es la matriz identidad
print("La primera matriz es la matriz identidad:", es_matriz_identidad(matriz_identidad))
print("La segunda matriz es la matriz identidad:", es_matriz_identidad(matriz_no_identidad))
