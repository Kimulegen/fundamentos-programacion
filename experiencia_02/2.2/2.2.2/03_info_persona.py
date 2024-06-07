#! Python3
# Ask for person info, show it formatted

name = input("Ingrese su nombre: ").upper()
rut = input("Ingrese su rut: ")
mail = input("Ingrese su email: ").upper()
phone = input("Ingrese su teléfono: ")

print(f"NOMBRE:     {name}\nRUT:        {rut}\nCORREO:     {mail}\nTELEFONO:   {phone}")
