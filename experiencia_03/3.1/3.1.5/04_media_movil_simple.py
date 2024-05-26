import random

# MIO
precios = []
for i in range(50):
    precios.append(random.randint(25,200))

periodos= 3
medias = []
for i in range(len(precios)-periodos+1):
    suma = 0
    for j in range(periodos):
        suma += precios[i+j]
    medias.append(round(suma / periodos))

# ALGO EJERCICIO
import random
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

precios = []
tiempo = []
media_movil = []

for t in range(51):
    precios.append(random.randint(1,20))
    tiempo.append(t)

periodos = 3

# FALTANTE
for conteo in range(len(precios)-periodos+1):
    promedio = 0
    for item in range(periodos):
        promedio += precios[item+conteo]
    promedio = round(promedio / periodos)
    media_movil.append(promedio)

for i in range(periodos -1):
    primero = media_movil[0]
    media_movil.insert(0,primero)

ax.plot(tiempo, precios)
ax.plot(tiempo,media_movil)
ax.set_title('Media Movil: Precio vs Tiempo')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Precio')

plt.show()