#! Python3
# A message function, example of default value for a parameter AND keyword arguments


def saludo(nombre, mensaje="Python"):
    print(mensaje, nombre)


saludo(mensaje="Buen día", nombre="Pedro")  # Buen día Pedro
