def suma_matrices(matriz1, matriz2):
    # Verifica si las matrices tienen las mismas dimensiones
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None  # Si no tienen las mismas dimensiones, devuelve None
    
    # Calcula el número de filas
    filas = len(matriz1)
    
    # Calcula el número de columnas
    columnas = len(matriz1[0])
    
    # Inicializa la matriz de suma como una lista vacía
    suma = []
    
    # Itera sobre cada fila
    for i in range(filas):
        # Inicializa una nueva fila para la matriz de suma
        fila_suma = []
        
        # Itera sobre cada columna
        for j in range(columnas):
            # Suma los elementos correspondientes de matriz1 y matriz2
            fila_suma.append(matriz1[i][j] + matriz2[i][j])
        
        # Añade la fila sumada a la matriz de suma
        suma.append(fila_suma)
    
    # Devuelve la matriz de suma
    return suma

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

# Llama a la función para sumar las matrices
resultado = suma_matrices(matriz1, matriz2)

# Verifica si las matrices tenían las mismas dimensiones
if resultado:
    # Imprime la matriz resultante
    for fila in resultado:
        print(fila)
else:
    # Imprime un mensaje de error si las matrices no tienen las mismas dimensiones
    print("Las matrices no tienen las mismas dimensiones.")
