def validar_lista_numeros(list):
    while True:
        numbers = list.strip().split(' ')
        try:
            for i in numbers:
                int(i)
        except ValueError:
            list = input('Ingrese una lista valida de numeros enteros separados por espacios')
            continue
        break
    return map(int,numbers)

numbers_list = validar_lista_numeros(input('Ingresa una lista de numeros enteros separados por espacios\n> '))

# LIST COMPREHENSION
# odds = [num for num in numbers_list if num % 2 == 1]
# evens = [num for num in numbers_list if num % 2 == 0]

# FOR LOOP
odds = []
evens = []
for i in numbers_list:
    evens.append(i) if i % 2 == 0 else odds.append(i)

print(f'Numeros pares: {evens}')
print(f'Numeros impares: {odds}')

