#! Python3
# Ask for 3 products' price and name, show the total of the sale

print("Ingresar los datos de la venta")
cliente = input("Ingrese el nombre del cliente")
precio_producto1 = input("Ingrese el precio del producto1")
cantidad_producto1 = input("Ingrese la cantidad del producto1")
precio_producto2 = input("Ingrese el precio del producto2")
cantidad_producto2 = input("Ingrese la cantidad del producto2")
precio_producto3 = input("Ingrese el precio del producto3")
cantidad_producto3 = input("Ingrese la cantidad del producto3")
descuento = input("Ingrese el descuento:")

total_bruto = precio_producto1 + precio_producto2 + precio_producto3
total_desc = total_bruto * (100 - descuento / 100)
iva = total_desc * 0.19
total = total_desc + iva
print(f"Cliente:      {cliente}")
print(f"Total Bruto:      {total_bruto}")
print(f"Total desc.:      {total_desc}")
print(f"Iva:      {iva}")
print(f"Total:        {total}")
