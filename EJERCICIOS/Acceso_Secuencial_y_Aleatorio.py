#ACCESO SECUENCIAL Y ALEATORIO EN UNA MATRIZ

# Matriz 5 filas y 5 columnas
matriz1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Matriz 3X3
matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


#Matriz 4X6
matriz3 = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24]
]

#Matrices existentes
matrices = [matriz1, matriz2, matriz3]

# Mostrar las matrices existentes
print("Matrices existentes:")
for i, matriz in enumerate(matrices, start=1):
    print(f"Matriz {i}:")
    for fila in matriz:
        print(fila)
    print()  # Salto de línea entre matrices

#Ingresar la matriz a recorrer 
matriz_seleccionada = int(input("Seleccione la matriz a recorrer (1, 2 o 3): "))
if matriz_seleccionada == 1:
    matriz = matriz1
elif matriz_seleccionada == 2:
    matriz = matriz2
elif matriz_seleccionada == 3:
    matriz = matriz3
else:
    print("Selección invalida. Se usara la matriz 1 por defecto.")
    matriz = matriz1


# Acceso secuencial a la matriz
print("Acceso secuencial")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()  # Salto de línea al final de cada fila



# Acceso aleatorio a la matriz
print("\nAcceso aleatorio")
numero_filas = len(matriz)
numero_columnas = len(matriz[0]) if matriz else 0
fila_aleatoria = int(input("Ingrese el numero de fila " + f"(0-{numero_filas-1}): "))
columna_aleatoria = int(input("Ingrese el número de columna " + f"(0-{numero_columnas-1}): "))
elemento_aleatorio = matriz[fila_aleatoria][columna_aleatoria]
print(f"\nElemento aleatorio seleccionado: {elemento_aleatorio} (Fila: {fila_aleatoria}, Columna: {columna_aleatoria})")    



