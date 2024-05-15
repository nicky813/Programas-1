numeros = list(range(1, 51))
print(numeros)

# Matriz
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for fila in matriz:
    print(fila)

filas = 8
columnas = 8

matriz = []

numero = 1
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(numero)
        numero += 1
    matriz.append(fila)

for fila in matriz:
    print(fila)
    
filas = 8
columnas = 8

matriz = [[i + j * columnas + 1 for i in range(columnas)] for j in range(filas)]

for fila in matriz:
    print(fila)

lista1=['Ana','Boris','Carlos','Doroti','Ema']
lista2=[24,50,80,28,21]
enumerate


def buscar (nombre):
    for indice, valor in enumerate(lista1):
        if nombre==valor:
            return(indice)
    
x=buscar('Doroti')
print(lista2[x])











