def multiplicar_matriz_escalar(matriz, escalar):
    # Inicializa la matriz resultante como una lista vacía
    resultado = []
    
    # Itera sobre cada fila de la matriz
    for fila in matriz:
        # Inicializa una nueva fila para la matriz resultante
        nueva_fila = []
        
        # Itera sobre cada elemento de la fila
        for elemento in fila:
            # Multiplica el elemento por el escalar y lo añade a la nueva fila
            nueva_fila.append(elemento * escalar)
        
        # Añade la nueva fila a la matriz resultante
        resultado.append(nueva_fila)
    
    # Devuelve la matriz resultante
    return resultado

# Ejemplo de uso:
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
escalar = 3

# Llama a la función para multiplicar la matriz por el escalar
resultado = multiplicar_matriz_escalar(matriz_ejemplo, escalar)

# Imprime la matriz resultante
for fila in resultado:
    print(fila)
