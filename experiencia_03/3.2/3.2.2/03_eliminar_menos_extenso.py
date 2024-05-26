names = []
while True:
    names.append(input('Ingrese un nombre\n> '))

    choice = input('Desea agregar otro nombre? (si/no)\n> ')
    if choice == 'no':
        break

names.sort(key=len)
names.pop(0)
print(names)
    