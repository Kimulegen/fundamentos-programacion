#! Python3
# Calculate clients purchases

# intitalize variables
productos = [
    "Tomate",
    "Leche",
    "Huevos",
    "Harina",
    "Levadura",
    "Mantequilla",
    "Queso",
    "Vienesas",
]
precios = [500, 900, 2500, 1000, 500, 2300, 4000, 3000]
total = 0

# ask for quantities of products
for index, item in enumerate(productos):
    print(item)
    print(f"${precios[index]}")
    cantidad = int(input("Ingrese cantidad: "))
    total += precios[index] * cantidad
    print()

# show total
print(" Detalle pago ".center(30, "-"))
print(f"Total afecto: {total}")
print(f"Iva: {total * 0.19}")
print(f"Total a pagar: {total * 1.19}")
