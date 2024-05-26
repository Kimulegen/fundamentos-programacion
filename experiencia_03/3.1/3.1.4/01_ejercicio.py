#promedioNotas 
sw = 1
listaNotas = []

print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")
op = int(input("Seleccione opción"))

if (op == 1):
    while sw == 1:
        try:
            print("---------------------------------------------------------")
            nota = int(input("Incorpore su nota, si desea salir, presione 0:"))
            if (nota != 0):
                listaNotas.append(nota)
                print('Notas ingresadas hasta ahora: ', " ".join(map(str,listaNotas)))
                print("Cantidad de notas ingresadas: ", len(listaNotas))
                promedioNotas = sum(listaNotas) / len(listaNotas)
                print(f"Promedio de notas: {promedioNotas:.{2}f}")
            else:
                print("Adiós")
                sw == 0
        except ValueError as ve:
            print(ve)
            print("Ingreso Erróneo")
else:
    print("Adiós")
