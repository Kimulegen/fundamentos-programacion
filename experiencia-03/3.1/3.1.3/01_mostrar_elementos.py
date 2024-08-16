#! Python3
# Ask for a matrix, show formatted matrix

import os

matrix_example = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# ask for size of matrix
rows = int(input("Ingrese el número de filas de su matriz\n> "))
cols = int(input("Ingrese el número de columnas de su matriz\n> "))
matrix = []

os.system("cls||clear")
# build matrix
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(input(f"Ingrese el número de la fila {i+1} y la columna {j+1}\n> "))
        os.system("cls||clear")
    matrix.append(row)

# show matrix
print("Su matriz:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
