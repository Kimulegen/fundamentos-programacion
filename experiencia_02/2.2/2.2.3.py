# EJERCICIO 1
nomAlum = input("Ingrese el nombre del alumno: ")
rut = input("Ingrese rut apoderado: ")
curso = input("Ingrese curso al cual el alumno debe matricularse: ")
matricula = int(25000)
mensualidad = int(30000)
resultadoAnual = (mensualidad*10)+matricula

print(f"-------Detalle Anualidad Colegio-------")
print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")
print(f"VALOR MATRÍCULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")

# EJERCICIO 2
producto = input("Ingrese el nombre del producto: ")
valorProducto = input("Ingrese el valor del producto: ")
valorNeto = float(0.81)
valorSinIva = float(valorProducto * valorNeto)
print(f"------Detalle producto------")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}")

# El tipo numérico  `float` permite representar un número positivo o negativo con decimales,
# es decir, número reales.
# Los valores float son almacenados de una forma muy particular, denominada representación
# en coma flotante.

# EJERCICIO 3
numero = 0
print(numero)
siguiente = 1
print (siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print (siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print (siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print (siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print (siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print (siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print (siguiente)
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print (siguiente)

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610