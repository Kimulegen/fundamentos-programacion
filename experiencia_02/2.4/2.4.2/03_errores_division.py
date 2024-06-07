#! Python
# Try to divide two numbers, catch errors

try:
    numerador = float(input("Ingrese el numerador\n> "))
    denominador = float(input("Ingrese el denominador\n> "))

    resultado = numerador / denominador

    print(f"El resultado de la división es: {resultado}")

except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero")
finally:
    print("Fin del programa")
