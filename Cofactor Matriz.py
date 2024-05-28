def submatriz(matriz, i, j):
    # Retorna una submatriz eliminando la fila i y la columna j
    return [fila[:j] + fila[j+1:] for fila in (matriz[:i] + matriz[i+1:])]

def determinante_matriz_2x2(matriz):
    # Calcula el determinante de una matriz 2x2
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

def cofactor(matriz, i, j):
    # Calcula el cofactor de la matriz en la posición (i, j)

    # Calcula el signo del cofactor según la regla de los signos alternados
    signo = (-1) ** (i + j)

    # Calcula el determinante de la submatriz
    det_submatriz = determinante_matriz_2x2(submatriz(matriz, i, j))

    # Retorna el cofactor multiplicando el determinante de la submatriz por el signo
    return signo * det_submatriz

# Ejemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
i = 1
j = 1

print("El cofactor en la posición ({}, {}) es:".format(i, j), cofactor(matriz, i, j))
