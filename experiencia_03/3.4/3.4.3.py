#! Python3
# A function that given a integers list, returns a list with odd numbers and another list with even numbers


# validation function
def validar_lista_numeros(list):
    while True:
        numbers = list.strip().split(" ")
        try:
            for i in numbers:
                int(i)
        except ValueError:
            list = input(
                "Ingrese una lista válida de números enteros separados por espacios"
            )
            continue
        break
    return map(int, numbers)


# print odd and even list
def show_odd_even(list):
    # FOR LOOP
    odd = []
    even = []
    for i in numbers_list:
        even.append(i) if i % 2 == 0 else odd.append(i)

    # LIST COMPREHENSION
    # odd = [num for num in numbers_list if num % 2 == 1]
    # even = [num for num in numbers_list if num % 2 == 0]

    print(f"Números pares: {even}")
    print(f"Números impares: {odd}")


numbers_list = validar_lista_numeros(
    input("Ingresa una lista de números enteros separados por espacios\n> ")
)

show_odd_even(numbers_list)
