#listaSuper
sw = 1
listaSuper = []
valorSuper = []

print("Presiones 1 para ingresar los productod del súper")
print("Presione cualquier tecla para salir")
op = int(input("Seleccione opción"))
if (op == 1):
    while sw == 1:
        try:
            print("----------------------------------------------------------")
            producto = input("Incorpore su producto, para salir, presione 0:")
            if(producto != 0):
                listaSuper.append(producto)
                valorSuper.append(int(input(f"Incorpore el valor del {producto}"))) 
                print('----DETALLE BOLETA-----')
                print(f'Productos comprados: {', '.join(listaSuper)}')
                print(f'Cantidad de productos comprados: {len(listaSuper)}')
                print(f'Suma de todos los productos: {sum(valorSuper)}')
            else:
                print("Adiós")
                sw = 0
        except:
            print("Ingreso Erróneo")
else:
    print("Adiós")