#! Python3
# A rest function, example of default values for the parameters


def resta(a=None, b=None):
    if a == None or b == None:
        print("Error, faltan parámetros a la función")
        return
    return a - b


resta()  # Error, faltan parámetros a la función
