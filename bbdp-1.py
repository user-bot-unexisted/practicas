import numpy as np

# Datos del variante 6
valores_variante = [19, 23, 29, 31]

# Crear matriz bidimensional 4x6 con números aleatorios entre 0 y 20
# Incluimos los números del variante en posiciones específicas
matriz = np.array([
    [5, 19, 8, 15, 3, 12],
    [23, 7, 14, 2, 29, 9],
    [11, 4, 31, 6, 18, 1],
    [16, 13, 10, 0, 22, 17]
])

print("Matriz original:")
print(matriz)
print()

# Reemplazar todos los elementos menores que 10 con 42
matriz_modificada = np.where(matriz < 10, 42, matriz)

print("Matriz modificada (elementos < 10 reemplazados por 42):")
print(matriz_modificada)