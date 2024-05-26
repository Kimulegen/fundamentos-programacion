#validaciónTipoDato
lista = ['Celular', 5000000, 'Computador', 4.3234, '$"#$$#%/&']
try:
    print('Identificación del elemento ingresado')
    for l in lista:
        if(lista[0] == 'Celular'):
            print(f'El elemento {l}, que se encuentra en la posición {lista.index(l)} de la lista, Es número')
        elif(lista[1] == 5000000):
            print(f'El elemento {l}, que se encuentra en la posición {lista.index(l)} de la lista, Es un número')
        elif(lista[2] == 'Computador'):
            print(f'El elemento {l}, que se encuentra en la posición {lista.index(l)} de la lista, Es un texto')
        else:
            print(f'El elemento {l}, que se encuentra en la posición {lista.index(l)} de la lista, Es indeterminado')
except:
    print('Problemas al leer los datos')

# ¿Qué diferencia tiene llamar a la lista como "L" (línea 5, línea 7) versus llamar como "lista[0] (línea 6)"
# 1. No hay ninguna diferencia entre ambas formas de llamar a la lista
# 2. Una es una lista, y otra es una sentencia de repetición
# 3. La primera forma llama por medio de un for al objeto, mientras que la segunda forma, llama al objeto entregando una posición exacta
# 4. Todas las opciones son correctas