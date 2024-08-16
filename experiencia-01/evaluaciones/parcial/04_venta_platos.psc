Algoritmo venta_platos
    Definir nombre_cliente Como Caracter
    Definir total, opcion como Entero
    Escribir "Ingrese su nombre"
    Leer nombre_cliente

    Repetir
        Escribir "Menú"
        Escribir "Opción 1. Arroz a la francesa - $3500"
        Escribir "Opción 2. Arroz marinero - $4.200"
        Escribir "Opción 3. Sopa marinera - $8.700"
        Escribir "Opción 4. Salir al menú general"
        Leer opcion
        Si opcion = 1 Entonces
            total = total + 3500
        SiNo
            Si opcion = 2 Entonces
                total = total + 4200
            SiNo
                Si opcion = 3 Entonces
                    total = total + 8700
                SiNo
                    Si opcion != 4 Entonces
                        Escribir "opción inválida, porfavor ingresar una opción válida"
                    FinSi
                    Esperar 1 Segundos
                FinSi
            FinSi
        FinSi
        Borrar Pantalla
        Escribir "valor de la boleta hasta ahora: ", total
    Hasta Que opcion = 4
    Borrar Pantalla
    Escribir "Sr/Sra ", nombre_cliente, ", el total a cobrar es: ", total
FinAlgoritmo