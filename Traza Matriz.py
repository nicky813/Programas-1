def calcular_traza(matriz):
    # Verifica si la matriz es cuadrada
    if len(matriz) != len(matriz[0]):
        return None  # Si la matriz no es cuadrada, no se puede calcular la traza
    
    # Inicializa la variable para almacenar la traza
    traza = 0
    
    # Itera sobre los elementos de la diagonal principal
    for i in range(len(matriz)):
        traza += matriz[i][i]  # Suma los elementos de la diagonal principal
    
    # Devuelve la traza calculada
    return traza

# Ejemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Llama a la función para calcular la traza
resultado_traza = calcular_traza(matriz)

# Verifica si la matriz era cuadrada y se pudo calcular la traza
if resultado_traza is not None:
    # Imprime la traza
    print("La traza de la matriz es:", resultado_traza)
else:
    # Imprime un mensaje de error si la matriz no es cuadrada
    print("La matriz no es cuadrada, no se puede calcular la traza.")
