import numpy as np

# datos
valores_variante = [19, 23, 29, 31]

# Crear matriz bidimensional 4x6 con números aleatorios entre 0 y 20
matriz = np.array([
    [5, 19, 8, 15, 3, 12],
    [23, 7, 14, 2, 29, 9],
    [11, 4, 31, 6, 18, 1],
    [16, 13, 10, 0, 22, 17]
])

print("Matriz original:")
print(matriz)
print()

# Reemplazar 10 por 42
matriz_modificada = np.where(matriz < 10, 42, matriz)

print("Matriz modificada:\t")
print(matriz_modificada)