
# permite multiplicar elementos de una matriz ingresadas por el usuario.
# Usar while for matrices trt/except validaciones funciones
# Menu de opciones para poder sumar matrices, multiplicar matrices y un boton para salir
def pretty_print(matrix):
    for row in matrix:
        print(" ".join(f"{num:4}" for num in row))

def get_matrix_dimensions(matrix):
    return (len(matrix),len(matrix[0]))

def sum_matrices(matrix1, matrix2):
    # Check matrices dimensions
    m1_dim= get_matrix_dimensions(matrix1)
    m2_dim= get_matrix_dimensions(matrix2)
    if m1_dim != m2_dim:
        print('Las dimensiones no coinciden!')
        return 0

    #sum
    result = []
    for i in range(m1_dim[0]):
        row = []
        for j in range(m1_dim[1]):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

def multiply_matrices(matrix1,matrix2):
    # Check dimensions
    m1_dim = get_matrix_dimensions(matrix1)
    m2_dim = get_matrix_dimensions(matrix2)
    if m1_dim[1] != m2_dim[0]:
        print('las dimensiones no coinciden')
        return 0
    
    # Multiply
    result = []
    for i in range(m1_dim[0]):
        row = []
        for j in range(m2_dim[1]):
            sum = 0
            for k in range(m1_dim[1]):
                sum += (matrix1[i][k] * matrix2[k][j])
            row.append(sum)
        result.append(row)
    
    return result

def multiply_matrix_scalar(matrix,scalar):
    result = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(i*scalar)
        result.append(new_row)
    
    return result

# def is_matrix_valid(matrix):
#     for row in matrix:
#         for i in row:
#             try:
#                 int(i)
#             except ValueError:
#                 return False
#     return True

def build_matrix():
    try:
        n_rows = int(input('Ingrese el numero de filas de su matriz\n> '))
        n_columns = int(input('Ingrese el numero de columnas de su matriz\n> '))

        matrix = []
        for i in range(n_rows):
            row =[]
            for j in range(n_columns):
                row.append(int(input(f'Ingrese el dato de la fila {i+1} y la columna {j+1}\n> ')))
            matrix.append(row)
        print('Su matriz construida es:')
        pretty_print(matrix)
        print()
        return matrix
    except ValueError:
        print('Error al construir su matriz, ingreso un dato no numerico')
        return 0

def main():
    while True:
        print('Bienvenido al menú')
        print('1. Sumar dos matrices')
        print('2. Multiplicar dos matrices')
        print('3. Multiplicar matriz por escalar')
        print('4. Salir')
        try:
            choice = int(input('> '))
        except ValueError:
            print('\nError, eleccion invalida\n')
            continue

        if choice == 1:
            m1 = build_matrix()
            m2 = build_matrix()

            if m1 == 0 or m2 == 0:
                print('No se pudo sumar las matrices')
                continue

            sum = sum_matrices(m1,m2)

            if sum == 0:
                print('No se pudo sumar las matrices')
                continue

            print('La suma de ambas matrices es:')
            pretty_print(sum)
            print()
        elif choice == 2:
            m1 = build_matrix()
            m2 = build_matrix()

            if m1 == 0 or m2 == 0:
                print('No se pudo multiplicar las matrices')
                continue

            mult = multiply_matrices(m1,m2)

            if mult == 0:
                print('No se pudo multiplicar las matrices')
                continue

            print('La multiplicacion de ambas matrices es:')
            pretty_print(mult)
            print()
        elif choice == 3:
            m1 = build_matrix()
            try:
                scalar = int(input('Ingrese el escalar\n> '))   
            except ValueError:
                print('Escalar ingresado no es un dato numerico')
                continue

            if m1 == 0:
                print('No se pudo multiplicar las matriz')
                continue

            mult = multiply_matrix_scalar(m1,scalar)

            print('La multiplicacion de la matriz por el escalar es:')
            pretty_print(mult)
            print()
        elif choice == 4:
            print('Adiós')
            break
        else:
            print('\nSeleccione una opcion valida\n')


if __name__ == '__main__':
    main()