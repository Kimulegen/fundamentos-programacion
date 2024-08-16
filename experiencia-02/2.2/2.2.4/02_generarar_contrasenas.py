#! Python3
# Generate passwords based on user input

print("Ingrese los siguientes datos:")
primer_nombre = input("Las 2 primeras letras de su primer nombre:")
segundo_apellido = input("Las 2 primeras letras de su segund apellido:")
rut = input("Los 2 primeros números de su rut:")
nacimiento = input("Las 3 letras iniciales del mes de su nacimiento:")
ciudad = input("Las 2 últimas letras de la ciudad donde vive:")

print(
    f"la opción 1 de contraseña es: {primer_nombre}{segundo_apellido}{rut}{nacimiento}{ciudad}"
)
print(
    f"la opción 2 de contraseña es: {primer_nombre}{rut}{segundo_apellido}{ciudad}{nacimiento}"
)
print(
    f"la opción 3 de contraseña es: {rut}{primer_nombre}{nacimiento}{ciudad}{segundo_apellido}"
)
print(
    f"la opción 4 de contraseña es: {segundo_apellido}{rut}{primer_nombre}{nacimiento}{ciudad}{rut}"
)
print(
    f"la opción 5 de contraseña es: {ciudad}{segundo_apellido}{primer_nombre}{rut}{nacimiento}{ciudad}"
)
