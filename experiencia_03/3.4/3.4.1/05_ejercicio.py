#! Python
# Demonstration of spread arguments


def calculo(precio, descuento):
    return precio - (precio * descuento) / 100


datos = [10000, 10]
print(
    "El monto final a pagar es: ", calculo(*datos)
)  # El monto final a pagar es:  9000.0
