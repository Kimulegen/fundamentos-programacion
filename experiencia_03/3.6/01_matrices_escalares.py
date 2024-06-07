#! Python3
# A program where you can sum matrices, multiply two matrices, and multiply a matrix by a scalar

import os


# format and print a matrix
def pretty_print(matrix):
    for row in matrix:
        print(" ".join(f"{num:4}" for num in row))


# get matrix dimensions
def get_matrix_dimensions(matrix):
    return (len(matrix), len(matrix[0]))


# sum two matrices
def sum_matrices(matrix1, matrix2):
    # Check matrices dimensions
    m1_dim = get_matrix_dimensions(matrix1)
    m2_dim = get_matrix_dimensions(matrix2)
    if m1_dim != m2_dim:
        print("Las dimensiones no coinciden!")
        return 0

    # sum
    result = []
    for i in range(m1_dim[0]):
        row = []
        for j in range(m1_dim[1]):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Check dimensions
    m1_dim = get_matrix_dimensions(matrix1)
    m2_dim = get_matrix_dimensions(matrix2)
    if m1_dim[1] != m2_dim[0]:
        print("las dimensiones no coinciden!")
        return 0

    # Multiply
    result = []
    for i in range(m1_dim[0]):
        row = []
        for j in range(m2_dim[1]):
            sum = 0
            for k in range(m1_dim[1]):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)

    return result


# multiply a matrix by a scalar
def multiply_matrix_scalar(matrix, scalar):
    result = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(i * scalar)
        result.append(new_row)

    return result


# build a matrix, ask for dimensions and values
def build_matrix():
    try:
        n_rows = int(input("Ingrese el número de filas de su matriz\n> "))
        n_columns = int(input("Ingrese el número de columnas de su matriz\n> "))

        matrix = []
        for i in range(n_rows):
            row = []
            for j in range(n_columns):
                os.system("cls||clear")
                row.append(
                    int(
                        input(
                            f"Ingrese el dato de la fila {i+1} y la columna {j+1}\n> "
                        )
                    )
                )
            matrix.append(row)
        os.system("cls||clear")
        print("Su matriz construida es:")
        pretty_print(matrix)
        print()
        return matrix
    except ValueError:
        print("Error al construir su matriz, ingresó un dato no numérico")
        return 0


# menu
def main():
    while True:
        print(" Bienvenido al menú ".center(40, "="))
        print("1. Sumar dos matrices")
        print("2. Multiplicar dos matrices")
        print("3. Multiplicar matriz por escalar")
        print("4. Salir")
        try:
            choice = int(input("> "))
        except ValueError:
            os.system("cls||clear")
            print("\nError, elección inválida\n")
            continue

        # sum two matrices
        if choice == 1:
            os.system("cls||clear")
            m1 = build_matrix()
            m2 = build_matrix()

            if m1 == 0 or m2 == 0:
                print("No se pudo sumar las matrices\n")
                continue

            sum = sum_matrices(m1, m2)

            if sum == 0:
                print("No se pudo sumar las matrices\n")
                continue

            os.system("cls||clear")
            print("La suma de ambas matrices es:")
            pretty_print(sum)
            print()

        # multiply two matrices
        elif choice == 2:
            os.system("cls||clear")
            m1 = build_matrix()
            m2 = build_matrix()

            if m1 == 0 or m2 == 0:
                print("No se pudo multiplicar las matrices")
                continue

            mult = multiply_matrices(m1, m2)

            if mult == 0:
                print("No se pudo multiplicar las matrices")
                continue

            os.system("cls||clear")
            print("La multiplicación de ambas matrices es:")
            pretty_print(mult)
            print()

        # multiply a matrix by a scalar
        elif choice == 3:
            os.system("cls||clear")
            m1 = build_matrix()
            try:
                scalar = int(input("Ingrese el escalar\n> "))
            except ValueError:
                print("Escalar ingresado no es un dato numérico")
                continue

            if m1 == 0:
                print("No se pudo multiplicar las matriz")
                continue

            mult = multiply_matrix_scalar(m1, scalar)

            os.system("cls||clear")
            print("La multiplicación de la matriz por el escalar es:")
            pretty_print(mult)
            print()

        # exit program
        elif choice == 4:
            print("Adiós")
            break

        # handle invalid options
        else:
            os.system("cls||clear")
            print("\nSeleccione una opción válida\n")


if __name__ == "__main__":
    main()
