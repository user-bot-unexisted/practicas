import numpy as np

# la matriz que vamos a usar
datos = np.array([
    [19, 5, 8, 15, 3, 23],
    [7, 23, 14, 2, 29, 9],
    [11, 4, 29, 6, 18, 1],
    [16, 13, 10, 0, 31, 17]
])

def mostrar_matriz():
    print("\nMatriz actual:")
    print(datos)
    print()

def suma_filas_columnas():
    print("\n--- Suma de filas y columnas ---")
    mostrar_matriz()
    
    # sumar filas
    filas = np.sum(datos, axis=1)
    print("Sumas por fila:")
    for idx, valor in enumerate(filas):
        print(f"  Fila {idx+1}: {valor}")
    
    # sumar columnas
    cols = np.sum(datos, axis=0)
    print("\nSumas por columna:")
    for idx, valor in enumerate(cols):
        print(f"  Columna {idx+1}: {valor}")

def intercambiar_columnas():
    print("\n--- Intercambiar primera y última columna ---")
    mostrar_matriz()
    
    copia = datos.copy()
    # cambiar primera por última
    copia[:, [0, -1]] = copia[:, [-1, 0]]
    
    print("Después del intercambio:")
    print(copia)

def diagonal_principal():
    print("\n--- Suma de la diagonal principal ---")
    mostrar_matriz()
    
    resultado = np.trace(datos)
    print(f"La suma de la diagonal es: {resultado}")

def reemplazar_elementos():
    print("\n--- Reemplazar elementos menores que la suma de la primera fila ---")
    mostrar_matriz()
    
    suma_primera = np.sum(datos[0])
    print(f"Suma de la primera fila: {suma_primera}")
    
    # reemplazar los que sean menores
    nueva = np.where(datos < suma_primera, suma_primera, datos)
    
    print("\nMatriz después del reemplazo:")
    print(nueva)

def filas_sin_ceros():
    print("\n--- Suma de elementos en filas sin ceros ---")
    mostrar_matriz()
    
    # encontrar filas que no tengan ceros
    indices = []
    for i in range(len(datos)):
        if 0 not in datos[i]:
            indices.append(i)
    
    print(f"Filas sin ceros: {[x+1 for x in indices]}")
    
    # sumar solo los positivos de esas filas
    total = 0
    for idx in indices:
        for num in datos[idx]:
            if num > 0:
                total += num
    
    print(f"Suma total de elementos positivos: {total}")

def menu():
    while True:
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL")
        print("="*50)
        print("1. Ver matriz")
        print("2. Sumar filas y columnas")
        print("3. Intercambiar columnas")
        print("4. Suma de diagonal principal")
        print("5. Reemplazar elementos")
        print("6. Filas sin ceros")
        print("0. Salir")
        print("="*50)
        
        opcion = input("\nElige una opción: ").strip()
        
        if opcion == "0":
            print("\n¡Hasta luego!")
            break
        elif opcion == "1":
            mostrar_matriz()
        elif opcion == "2":
            suma_filas_columnas()
        elif opcion == "3":
            intercambiar_columnas()
        elif opcion == "4":
            diagonal_principal()
        elif opcion == "5":
            reemplazar_elementos()
        elif opcion == "6":
            filas_sin_ceros()
        else:
            print("\nOpción no válida, intenta de nuevo")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu()