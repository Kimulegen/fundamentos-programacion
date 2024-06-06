#! Python3
# Ask for a matrix, show formatted matrix

matrix_example = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# ask for size of matrix
rows = int(input("Ingrese el número de filas de su matriz"))
cols = int(input("Ingrese el número de columnas de su matriz"))
matrix = []

# build matrix
for i in range(rows)
    row = []
    for j in range(cols)
        row.append(input(f"Ingrese el número de la fila {i} y la columna {j}"))
    matrix.append(row)

# show matrix
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
