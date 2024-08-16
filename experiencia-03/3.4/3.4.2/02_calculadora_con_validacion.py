#! Python3
# A calculator function and a validation function to sanitize user input


# calculator function
def calculator(a, b):
    def sum(a, b):
        return a + b

    def rest(a, b):
        return a - b

    def mult(a, b):
        return a * b

    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("No se puede dividir por cero!")
            return "invalid"

    operacion = input(
        "Indique la operacion que desea hacer (sumar/restar/multiplicar/dividir)\n> "
    )
    match operacion:
        case "sumar":
            print("La suma de los numeros es:", sum(a, b))
        case "restar":
            print("La resta de los numeros es:", rest(a, b))
        case "multiplicar":
            print("La multiplicacion de los numeros es:", mult(a, b))
        case "dividir":
            print("La division de los numeros es:", divide(a, b))
        case _:
            print("operacion no valida")
            return


# validation function
def validar(n):
    while True:
        try:
            fl = float(n)
            return fl
        except ValueError:
            print("Error! ingrese un numero valido")
            n = input("Reingrese el numero\n> ")


a = validar(input("Ingrese primer numero\n> "))
b = validar(input("Ingrese segundo numero\n> "))

calculator(a, b)
