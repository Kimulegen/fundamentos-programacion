# Bubble sort algorithm

## Mi respuesta
```python
import random

lista = []
for i in range(1000):
    lista.append(random.randint(1, 10000))

for i in range(len(lista) - 1):
    for j in range(i, -1, -1):
        if lista[j + 1] < lista[j]:
            tmp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = tmp
        else:
            break
```

# MIO TAMBIEN
for i in range(len(lista) - 1):
    for j in range(0, i + 1):
        if lista[i - j + 1] < lista[i - j]:
            tmp = lista[i - j]
            lista[i - j] = lista[i - j + 1]
            lista[i - j + 1] = tmp
        else:
            break

# ALGO EJERCICIO
import random

arreglo = []

for ciclo in range(50):
    aleatorio = random.randint(1, 1000)
    arreglo.append(aleatorio)

print("")
print("Arreglo Original")
print(arreglo)
print("")

largo_arreglo = len(arreglo)

# SECCION FALTANTE

print("")
print("Arreglo Ordenado")
print(arreglo)

if largo_arreglo % 2 == 0:
    mediana = (arreglo[int(largo_arreglo / 2) - 1]) + arreglo[
        int(largo_arreglo / 2)
    ] / 2
else:
    mediana = arreglo[round(int(largo_arreglo / 2))]
print("Mediana: ", mediana)

# OPCION 1
for i in range(largo_arreglo - 1):
    for j in range(largo_arreglo - 1 - i):
        if arreglo[j] < arreglo[j + 1]:
            temporal = arreglo[j]
            arreglo[j] = arreglo[j + 1]
            arreglo[j + 1] = temporal
# OPCION 2
for i in range(largo_arreglo - 1):
    for j in range(largo_arreglo - 1 - i):
        if arreglo[j] > arreglo[j + 1]:
            arreglo[j] = arreglo[j + 1]
            arreglo[j + 1] = arreglo[j]
# OPCION 3
for i in range(largo_arreglo - 1):
    for j in range(largo_arreglo - 1 - i):
        if arreglo[j] < arreglo[j + 1]:
            temporal = arreglo[j]
            arreglo[j] = arreglo[j + 1]
            arreglo[j + 1] = arreglo[j]
# OPCION 4 (solucion)
for i in range(largo_arreglo - 1):
    for j in range(largo_arreglo - 1 - i):
        if arreglo[j] > arreglo[j + 1]:
            temporal = arreglo[j]
            arreglo[j] = arreglo[j + 1]
            arreglo[j + 1] = temporal
