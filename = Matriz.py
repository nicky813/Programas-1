def son_iguales(matriz1, matriz2):
    # Verifica si las dimensiones de las matrices son iguales
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return False  # Si las dimensiones no son iguales, las matrices no son iguales
    
    # Itera sobre cada fila y columna de las matrices
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            # Compara los elementos correspondientes de ambas matrices
            if matriz1[i][j] != matriz2[i][j]:
                return False  # Si hay algún elemento diferente, las matrices no son iguales
    
    # Si se recorren todos los elementos y son iguales, las matrices son iguales
    return True

# Ejemplo de uso:
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Llama a la función para verificar si las matrices son iguales
resultado = son_iguales(matriz1, matriz2)

# Imprime el resultado
print("Las matrices son iguales:", resultado)

# Otro ejemplo con matrices diferentes
matriz3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10]
]

# Llama a la función para verificar si las matrices son iguales
resultado = son_iguales(matriz1, matriz3)

# Imprime el resultado
print("Las matrices son iguales:", resultado)
