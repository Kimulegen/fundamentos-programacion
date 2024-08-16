#! Python3
# Count number of color ocurrences in multidimensional matrix

import random

# initialize variables
colors = ("Amarillo", "Rojo", "Naranja", "Verde", "Blanco")
amarillo = rojo = naranja = verde = blanco = 0

# build matrix filled with colors at random
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        column = []
        for k in range(3):
            column.append(random.choice(colors))
        row.append(column)
    matrix.append(row)

# count ocurrence of colors, store it in counters
for row in matrix:
    for column in row:
        for item in column:
            match item:
                case "Amarillo":
                    amarillo += 1
                case "Rojo":
                    rojo += 1
                case "Naranja":
                    naranja += 1
                case "Verde":
                    verde += 1
                case "Blanco":
                    blanco += 1

# show number of ocurrence of each color
print("Número de elementos 'amarillo':", amarillo)
print("Número de elementos 'rojo':", rojo)
print("Número de elementos 'naranja':", naranja)
print("Número de elementos 'verde:'", verde)
print("Número de elementos 'blanco':", blanco)
