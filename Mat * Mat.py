def multiplicar_matrices(matriz1, matriz2):
    # Verifica si el número de columnas de la primera matriz es igual al número de filas de la segunda matriz
    if len(matriz1[0]) != len(matriz2):
        return None  # Si no son iguales, no se pueden multiplicar las matrices
    
    # Inicializa la matriz resultante con ceros
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]
    
    # Itera sobre cada fila de la primera matriz
    for i in range(len(matriz1)):
        # Itera sobre cada columna de la segunda matriz
        for j in range(len(matriz2[0])):
            # Itera sobre cada elemento de la fila de la primera matriz y la columna de la segunda matriz
            for k in range(len(matriz2)):
                # Realiza la multiplicación y suma los productos
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    # Devuelve la matriz resultante
    return resultado

# Ejemplo de uso:
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Llama a la función para multiplicar las matrices
resultado = multiplicar_matrices(matriz1, matriz2)

# Verifica si las matrices se podían multiplicar
if resultado:
    # Imprime la matriz resultante
    for fila in resultado:
        print(fila)
else:
    # Imprime un mensaje de error si las matrices no se podían multiplicar
    print("Las matrices no se pueden multiplicar debido a dimensiones incompatibles.")
