# Crear una matriz bidimensional (3x3)
matriz = [
    [10, 80, 40],
    [8, 2, 4],
    [9, 50, 30]
]

# Función para ordenar una fila específica  ascendente
# Algoritmo de ordenación Bubble Sort

def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos

# Función para mostrar la matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original

print("Matriz Original:")
mostrar_matriz(matriz)

# Ordenar solo la primera fila utilizando Bubble Sort

bubble_sort_fila(matriz[0])

# Mostrar la matriz con la primera fila ordenada

print("\nMatriz con la primera fila ordenada:")
mostrar_matriz(matriz)