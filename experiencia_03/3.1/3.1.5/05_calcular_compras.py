productos = ["Tomate", "Leche","Huevos","Harina","Levadura", "Mantequilla","Queso","Vienesas"]
precios = [500,900,2500,1000,500,2300,4000,3000]

total = 0
for index,item in enumerate(productos):
    print(item)
    print(precios[index])
    cantidad = int(input("Ingrese cantidad: "))
    total += precios[index] * cantidad

print("Detalle pago:")
print(f"Total afecto: {total}")
print(f"Iva: {total * 0.19}")
print(f"Total a pagar: {total * 1.19}")