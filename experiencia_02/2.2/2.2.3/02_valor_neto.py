#! Python3
# Calculate net value of a product

producto = input("Ingrese el nombre del producto: ")
valorProducto = input("Ingrese el valor del producto: ")
valorNeto = float(0.81)
valorSinIva = float(valorProducto * valorNeto)
print(f"------Detalle producto------")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}")
