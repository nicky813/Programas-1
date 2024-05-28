def matriz_identidad(n):
    # Inicializa una matriz vacía
    identidad = []

    # Itera sobre las filas de la matriz
    for i in range(n):
        # Inicializa una fila vacía
        fila = []
        # Itera sobre las columnas de la fila
        for j in range(n):
            # Agrega 1 si estamos en la diagonal principal, 0 en otro caso
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        # Agrega la fila a la matriz identidad
        identidad.append(fila)

    return identidad

# Ejemplo de uso:
n = 4
mi_matriz_identidad = matriz_identidad(n)
print("Matriz Identidad de tamaño", n, "x", n, ":")
for fila in mi_matriz_identidad:
    print(fila)
