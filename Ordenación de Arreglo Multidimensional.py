def ordenar_fila(matriz, fila):
    # Verificar si la fila está dentro de los límites de la matriz
    if fila < 0 or fila >= len(matriz):
        print("Fila no válida.")
        return

    # Aplicar el algoritmo de Bubble Sort a la fila seleccionada
    matriz[fila] = bubble_sort(matriz[fila])

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# Definir una matriz 3x3 (puede cambiar los valores según tus necesidades)
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar una fila para ordenar (por ejemplo, la primera fila con índice 0)
fila_a_ordenar = 0
ordenar_fila(matriz, fila_a_ordenar)
# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
