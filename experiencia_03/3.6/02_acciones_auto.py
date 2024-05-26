# acciones
# encender auto, colocar alarma, auto encendido, auto estacionado, auto con nivel de aceite bajo
# usar while for listas try/except validaciones, archivo CSV y funciones.
# menu de opciones para poder agregar acciones a la bitacora texto:
# la segunda opcion es para ver las acciones hechas en el auto
# la tercera opcion guarda la bitacora en un archivo CSV 
# la cuarta opcion es para salir
# Las acciones se registran con la fecha y hora actual en el formato 'dd-mm-yyyy HH:MM:SS' utilizar libreria from datetime import datetime
# El usuario debe guardar el archivo CSV con el nombre y extension
# Si el archivo CSV ya existe, se debe sobreescribir
import csv
from datetime import datetime

bitacora = []

def main():
    while True:
        print('*'*15,'Bienvenido al menú, seleccione su opción','*'*15)
        print('1. Agregar acción')
        print('2. Ver bitácora')
        print('3. Guardar bitácora')
        print('4. Salir')
        try:
            choice = int(input('> '))
        except ValueError:
            print()
            print('Error, favor ingrese un dato numérico')
            
        print()
        if choice == 1:
            action = input('¿Qué acción desea agregar?\n> ')
            formatted_datetime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            bitacora.append([formatted_datetime, action])
            print()
            print('Acción agregada')
            

        elif choice == 2:
            print('*'*15, 'Bitácora del auto','*'*15)
            if len(bitacora) == 0:
                print('No hay acciones registradas por el momento')
            else:
                for fecha,action in bitacora:
                    print(fecha,action)
            
        elif choice == 3:
            file_name = input('Ingrese el nombre del archivo al cual desea guardar la bitácora\n> ')
            file_name = file_name if len(file_name) > 0 else 'bitacora'
            fieldnames = ['fecha', 'accion']
            with open(f'{file_name}.csv', 'w+', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows({'fecha': action[0], 'accion': action[1]} for action in bitacora)
                print('Bitácora guardada con éxito')
        elif choice == 4:
            print('Saliendo del menú')
            break
        else:
            print('Favor ingresar una opción válida')
        print()

if __name__ == '__main__':
    main()