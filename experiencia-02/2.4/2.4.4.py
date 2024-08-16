#! Python3
# Total ticket sales

n_pasajes = int(input("¿Cuántos pasajes deseas vender? "))
total_ingresos = 0

for i in range(1, n_pasajes + 1):
    try:
        precio = int(input(f"Ingresa el precio del pasaje {i} "))
        total_ingresos += precio
    except ValueError as ve:
        print("Error, valor ingresado no es un número")
        break

print(f"El total de la venta es {total_ingresos}")
