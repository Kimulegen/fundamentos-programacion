# EJERCICIO 1
nom = input("Ingrese nombre empleado: ")
rut = input("Ingrese rut empleado: ")
horasTrabajadas = input("Ingrese las horas trabajadas: ")
valorHora = input("Ingrese el valor hora del empleado: ")
colacion = int(5500)
movilizacion = int(3000)
resultado = (valorHora * horasTrabajadas)+colacion+movilizacion

print(f"-----LIQUIDACION EMPLEADO-----")
print(f"NOMBRE EMPLEADO: {nom}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACIÓN: {movilizacion}")
print(f"ALIMENTACIÓN: {colacion}")
print(f"PAGO A EMPLEADO: {resultado}")

# EJERCICIO 2
print("Ingrese los siguientes datos:")
primer_nombre = input("Las 2 primeras letras de su primer nombre:")
segundo_apellido = input("Las 2 primeras letras de su segund apellido:")
rut = input("Los 2 primeros números de su rut:")
nacimiento = input("Las 3 letras iniciales del mes de su nacimiento:")
ciudad = input("Las 2 últimas letras de la ciudad donde vive:")

print(f"la opción 1 de contraseña es: {primer_nombre}{segundo_nombre}{rut}{nacimiento}{ciudad}")
print(f"la opción 2 de contraseña es: {primer_nombre}{rut}{segundo_nombre}{ciudad}{nacimiento}")
print(f"la opción 3 de contraseña es: {rut}{primer_nombre}{nacimiento}{ciudad}{segundo_apellido}")
print(f"la opción 4 de contraseña es: {segundo_apellido}{rut}{primer_nombre}{nacimiento}{ciudad}{rut}")
print(f"la opción 5 de contraseña es: {ciudad}{segundo_nombre}{primer_nombre}{rut}{nacimiento}{ciudad}")

# EJERCICIO 3
posicion1="x"
posicion2=""
posicion3=""
posicion4=""
posicion5="x"
posicion6=""
posicion7=""
posicion8=""
posicion9="x"

print(f"        {posicion1}         |       {posicion2}         |        {posicion3}         "
print("--------------------------------------------------------------------------------------"
print(f"        {posicion4}         |       {posicion5}         |        {posicion6}         "
print("--------------------------------------------------------------------------------------"
print(f"        {posicion7}         |       {posicion8}         |        {posicion9}         "

# EJERCICIO 4
print("Ingresar los datos de la venta")
cliente=input("Ingrese el nombre del cliente")
precio_producto1=input("Ingrese el precio del producto1")
cantidad_producto1=input("Ingrese la cantidad del producto1")
precio_producto2=input("Ingrese el precio del producto2")
cantidad_producto2=input("Ingrese la cantidad del producto2")
precio_producto3=input("Ingrese el precio del producto3")
cantidad_producto3=input("Ingrese la cantidad del producto3")
descuento=input("Ingrese el descuento:")

total_bruto = precio_producto1+precio_producto2+precio_producto3}
total_desc = total_bruto*(100-descuento / 100)
iva = total_desc * 0.19
total = total_desc + iva
print(f"Cliente:      {cliente}")
print(f"Total Bruto:      {total_bruto}")
print(f"Total desc.:      {total_desc}")
print(f"Iva:      {iva}")
print(f"Total:        {total}")

# EJERCICIO 5
print("")
linea1 = ("          ___      |\________/)")
linea18 =("          [_,_])    \ /       \|")
linea11 =("         /|=T=|]     /   __  __\\")
linea13 =("         |\ ' //     |_  9   p ]\\")
linea15 =("         ||'-'/--.  / /\\ =|  \|\\ \\")
linea16 =("        /|| <\/> |\ | '._, @ @)<_)")
linea21 =("       | |\   |  |   \.__/(_;_)")
linea31 =("       |  .   H  |   |  :  '='|")
linea6 =("       |  |  _H__/  _| :      |")
linea7 =("        \  '.__  \ /  ;      ';")
linea19 =("       __'-._(_}==.'  :       ;")
linea71 =("      (___|    /-' |   :.     :")
linea371 =("     [.-'  \   |   \   \ ;   :")
linea2 =("    .-'     |  |    |  |   ':")
linea22 =("   /        |==|     \  \  /  \_")
linea661 =("  /         [  |      '._\_ -._ \\")
linea517 =(" /           \__)   __.- \ \   )\\")
linea81 =("/       |        /.'      >>)")
linea61 =("|        \       |\     |")
linea414 =("|     .'  '-.    | \    /")
linea651 =("|    /     /     / /   /")
linea51 =("           |    /")
linea41 =("")


print(linea1)
print(linea18)
print(linea11)
print(linea13)
print(linea15)
print(linea16)
print(linea21)
print(linea31)
print(linea6)
print(linea7)
print(linea19)
print(linea71)
print(linea371)
print(linea2)
print(linea22)
print(linea661)
print(linea517) 
print(linea81) 
print(linea61) 
print(linea414) 
print(linea651)
print(linea51) 
print(linea41) 



