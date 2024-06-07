#! Python3
# Ask for employee info, show it formatted

nom = input("Ingrese nombre empleado: ")
rut = input("Ingrese rut empleado: ")
horasTrabajadas = input("Ingrese las horas trabajadas: ")
valorHora = input("Ingrese el valor hora del empleado: ")
colacion = int(5500)
movilizacion = int(3000)
resultado = (valorHora * horasTrabajadas) + colacion + movilizacion

print(f"-----LIQUIDACION EMPLEADO-----")
print(f"NOMBRE EMPLEADO: {nom}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACIÓN: {movilizacion}")
print(f"ALIMENTACIÓN: {colacion}")
print(f"PAGO A EMPLEADO: {resultado}")
